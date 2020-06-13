from django.shortcuts import render, get_object_or_404
from .models import Post


# View showing list of blog entries
def post_list(request):
    # Retrive all published posts using the published model manager
    posts = Post.published.all()

    return render(request, 'blog/post/list.html', {
        'posts': posts})


# View to show details of a single blog post
def post_detail(request, year, month, day, post):
    # Find the blog post matching the parameters or return a 404
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {
        'post': post})
