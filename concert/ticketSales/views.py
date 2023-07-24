from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse
from ticketSales.models import concertModel, locationModel, timeModel
from django.contrib.auth.decorators import login_required
from ticketSales.forms import SearchForm, ConcertForm
from django.contrib.auth.decorators import login_required
from .models import concertModel, locationModel, timeModel
from .forms import SearchForm, ConcertForm

def home(request):
    # Renders the home.html template
    return render(request, 'ticketSales/home.html')

def profile(request):
    # Renders the profile.html template
    return render(request, 'ticketSales/profile.html')

def concertListView(request):
    # Get the search form from the request
    searchForm = SearchForm(request.GET)
    
    # Check if the form is valid
    if searchForm.is_valid():
        # Get the search criteria from the form
        ConcertName = searchForm.cleaned_data['concertName']
        SingerName = searchForm.cleaned_data['singerName']
        
        # Filter concerts based on the search criteria
        concerts = concertModel.objects.filter(Name__contains=ConcertName, SingerName__contains=SingerName)
    else:
        # If the form is not valid, get all concerts
        concerts = concertModel.objects.all()
    
    context = {
        'concertlist': concerts,
        'searchForm': searchForm
    }
    
    # Renders the concertlist.html template with the concerts and search form
    return render(request, 'ticketSales/concertlist.html', context)

def locationListView(request):
    # Get all locations from the database
    locations = locationModel.objects.all()
    
    context = {
        'locationlist': locations,
    }
    
    # Renders the locationlist.html template with the locations
    return render(request, 'ticketSales/locationlist.html', context)

def concertDetailsView(request, concert_id):
    # Get the concert with the specified ID from the database
    concert = concertModel.objects.get(pk=concert_id)
    
    context = {
        'concertdetails': concert,
    }
    
    # Renders the concertdetails.html template with the concert details
    return render(request, 'ticketSales/concertdetails.html', context)

@login_required
def timeView(request):
    # Get all times from the database
    times = timeModel.objects.all()

    context = {
        'timelist': times,
    }
    
    # Renders the timelist.html template with the times
    return render(request, 'ticketSales/timelist.html', context)

def concertEditView(request, concert_id):
    # Get the concert with the specified ID from the database
    concert = concertModel.objects.get(pk=concert_id)

    if request.method == 'POST':
        # If the form is submitted, process the form data
        concertForm = ConcertForm(request.POST, request.FILES, instance=concert)
        if concertForm.is_valid():
            # Save the changes to the concert object
            concertForm.save()
            # Redirect to the concert list view after saving
            return HttpResponseRedirect(reverse('ticketSales:concertListView'))
    else:
        # If the form is not submitted, create a new form instance with the concert data
        concertForm = ConcertForm(instance=concert)
    
    context = {
        'concertForm': concertForm,
        'PosterImage': concert.Poster,
    }

    # Renders the concertEdit.html template with the concert form and poster image
    return render(request, 'ticketSales/concertEdit.html', context)
