from django import forms


class ScrapeForm(forms.Form):
    link = forms.CharField(label="Link to scrape", max_length=500)
    recursive = forms.CharField(
        label="Recursive", required=False, widget=forms.CheckboxInput
    )
