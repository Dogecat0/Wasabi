import re
from typing import List
from urllib.parse import urljoin, urlparse

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

is_fname = re.compile(r"\w+\.\w+")


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


def preprocess_url(link: str, with_path=False, with_fname=False):
    parsed = urlparse(link)
    url = f"{parsed.scheme}://{parsed.netloc}"
    if with_path:
        path = parsed.path.split("/")
        if not with_fname:
            path = path[:-1] if is_fname.match(path[-1]) else path
        path = "/".join(path)
        url += path
    return url


def scrape(info):
    queue = [info["link"]]
    done = set()
    links = set()

    while queue:
        target = queue.pop()
        target = preprocess_url(target, with_path=True, with_fname=False)
        if target in done:
            continue
        else:
            done.add(target)

        found: List[str] = extract_links(target)
        found = [
            preprocess_url(item, with_path=True, with_fname=True) for item in found
        ]
        links.update(found)

        if info["recursive"]:
            queue.extend(found)
        print(f"LINKS: {len(links)} QUEUE: {len(queue)}")

    scraped = [(link, scrape_me(link, wild_mode=info["wild_mode"])) for link in links]
    for link, item in scraped:
        Scraped(link=link, content=item.page_data).save()
    return


# Extract all links from a given url page
def extract_links(target: str) -> set:
    # Get link (inc query etc.) content
    reqs = requests.get(target)

    # Parse for hrefs
    soup = BeautifulSoup(reqs.text, "html.parser")
    found_href = soup.find_all(href=True, recursive=True)
    found = set()
    for item in found_href:
        href: str = item.get("href", "")
        if not validators.url(href, public=True):
            href = urljoin(target, href)
        if not href.startswith(target):
            continue
        found.add(href)
    return found


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
