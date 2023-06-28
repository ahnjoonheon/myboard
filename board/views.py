from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-pub_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post_detail.html' # <app>/<model>_<viewtype>.html

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})
