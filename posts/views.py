from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Post


def post_list_view(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/post_list.html', context)


def post_detail_view(request, id):
    if id is not None:
        post_detail = Post.objects.get(id=id)
    else:
        raise Http404()

    context = {
        'post_detail': post_detail
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.user
        if title and description:
            new_post = Post.objects.create(title=title, description=description, author=author)
            return redirect('post-detail', new_post.id)
    return render(request, "posts/post_create.html")


@login_required
def like_view(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes.add(request.user)
    return redirect('post-list')