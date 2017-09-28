from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text = """<h1>Bienvenue sur le site des crepes bretonnes</h1>
              <p>Les crepes bretonnes ca tue des mouettes en plein vol</p>"""
    return HttpResponse(text)
