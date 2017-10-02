from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def home(request):
    """List all articles on home page"""
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'last_articles': articles})

def read(request, article_id):
    """Display a whole article"""
    pass
