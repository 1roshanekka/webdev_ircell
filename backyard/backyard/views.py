# I have made this file - Roshan Ekka 
import re
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''<a href="https://1roshanekka.github.io/ircell-task/">Open</a>''')

def data(request):
    return HttpResponse("DataBase are shown here")

def about(request):
    return HttpResponse("About")