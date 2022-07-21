from django.shortcuts import render, get_object_or_404
from .models import Post, Group


FILTER = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:FILTER]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.group.related_name.order_by('-pub_date')[:FILTER]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
