from django import forms
from ticketSales.models import concertModel

class SearchForm(forms.Form):
    concertName = forms.CharField(max_length=100, label="Concert Name", required=False)
    singerName = forms.CharField(max_length=100, label="Singer Name", required=False)

    # A search form for filtering concerts based on concert name and singer name.

class ConcertForm(forms.ModelForm):
    class Meta:
        model = concertModel
        fields = ['Name', 'SingerName', 'length', 'Poster']

        