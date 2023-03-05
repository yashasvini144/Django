from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

"""
As you can see, we created a function (def) called post_list that takes request and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html.
"""

"""
A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template. We'll create a template in the next chapter. Views are just Python functions that are a little bit more complicated than the ones we wrote in the Introduction to Python chapter.
"""