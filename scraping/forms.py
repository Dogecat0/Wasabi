from django import forms


class ScrapeForm(forms.Form):
    link = forms.CharField(label="Link to scrape", max_length=500)
    recursive = forms.CharField(
        label="Recursive", required=False, widget=forms.CheckboxInput
    )
    wild_mode = forms.CharField(
        label="Wild mode", required=False, widget=forms.CheckboxInput
    )


class DefaultLinksForm(forms.Form):
    links = forms.ChoiceField(
        label="Default Links", required=False, help_text="Select a default link"
    )
