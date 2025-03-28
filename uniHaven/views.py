from django.http import HttpResponse
from django.shortcuts import render
from uniHaven.models import Accommodation

def hello(request):
    return HttpResponse('Hello, user!') 

def accommodation_list(request):
    context = {
        "accommodations": Accommodation.objects.all()
    }
    return render(request, 'accommodation_list.html', context=context)