from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here
from .forms import ScrapeForm


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
    return render(request, "index.html", {"form": form})


def scrape(info):
    return info
