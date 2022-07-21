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
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:FILTER]
    # Попробовал напрямую запросить посты из группы.
    # posts = Post.group.related_name.order_by('-pub_date')[:FILTER]
    # при запуски сайта проблем не возникало.
    # Во время запуска тестов возникла ошибка
    # AttributeError:
    # 'ForwardManyToOneDescriptor' object has no attribute 'related_name'

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
