from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})