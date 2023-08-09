from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Flight

# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
