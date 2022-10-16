from urllib.parse import urljoin

import requests
import validators
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render
from recipe_scrapers import SCRAPERS, scrape_me
from recipes.models import Recipe

# Create your views here
from .forms import DefaultLinksForm, ScrapeForm
from .models import Scraped


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ScrapeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            scrape(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/scraping/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScrapeForm()
    return render(request, "scraping/scraping.html", {"form": form})


def scrape(info):
    links = [info["link"]]
    if info["recursive"]:
        links = extract_links(info["link"])
    scraped = [(link, scrape_me(link, wild_mode=info["wild_mode"])) for link in links]
    for link, item in scraped:
        Scraped(link=link, content=item.page_data).save()
    return


# Extract all links from a given url page


def extract_links(link: str):

    reqs = requests.get(link)
    soup = BeautifulSoup(reqs.text, "html.parser")

    links = []
    for url in soup.find_all("a", recursive=True):
        url: str = url.get("href")
        if not url.startswith(link) and not validators.url(link):
            url = urljoin(link, url)
        links.append(url)
    return links


def default_links(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DefaultLinksForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            get_default_links(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/default_links/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DefaultLinksForm()
    return render(request, "default_links.html", {"form": form})


def get_default_links(scrapers):
    links = scrapers["links"]
