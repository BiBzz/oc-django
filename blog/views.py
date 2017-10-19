from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
    """List all posts on home page"""
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'last_posts': posts})

def read(request, post_id, post_slug):
    """Display a whole post"""
    post = get_object_or_404(Post, id=post_id, slug=post_slug)
    return render(request, 'blog/post.html', {'post': post})
