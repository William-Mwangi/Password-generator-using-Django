from django.shortcuts import render #render is used to display data from templates
from django.http import HttpResponse #function return value must be formatted as a HTTP response
import random

# Create your views here.
# def home(request):
#     return HttpResponse('hello there user')  #to produce a string onto the html page

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thePass = ''
    #length = 10
    userLength = int(request.GET.get('length')) #transformed to int so as to be able to use it as an iterable in the for loop
    userNumber = request.GET.get('numbers')
    userCapital = request.GET.get('uppercase')
    userSpecial = request.GET.get('specials')
    #check if user wants upper case letters
    if userCapital:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if userNumber:
        characters.extend(list('0123456789'))
    if userSpecial:
        characters.extend(list('!@#$%^&*<>?/\|`~'))
    for cha in range(userLength):
        thePass= thePass+ random.choice(characters)
    return render(request, 'generator/password.html', {'password':thePass})


def home(request):
    return render(request, 'generator/home.html') #displays whatever is in the template to the url being requested
    #we can even pass data to the templates themselves from this views.py

def about(request):
    return render(request, 'generator/about.html')
