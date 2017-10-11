from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
    """List all posts on home page"""
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'last_posts': posts})

def read(request, post_id):
    """Display a whole post"""
    pass
