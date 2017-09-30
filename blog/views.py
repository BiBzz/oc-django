from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def home(request):
    text = """<h1>Bienvenue sur le site des crepes bretonnes</h1>
              <p>Les crepes bretonnes ca tue des mouettes en plein vol</p>"""
    return HttpResponse(text)

def view_article(request, id_article):
    text = "Vous avez demandé l'article {0}".format(id_article)
    return HttpResponse(text)

def list_articles(request, year, month):
    text = "Vous avez demandé la liste des articles du mois {0}/{1}".format(month, year)
    return HttpResponse(text)

def today_date(request):
    return render(request, 'blog/date.html', {'today_date':datetime.now()})
