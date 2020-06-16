"""Defines the apps views"""

from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Post
from .forms import EmailPostForm


class PostListView(ListView):
    """Class-based view to show list of blog entries"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    """View to show details of a single blog post"""

    # Find the blog post matching the parameters or return a 404
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {
        'post': post})

def post_share(request, post_id):
    """View to share a blog post by email"""

    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields pass validation
            cleaned = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cleaned['name']} recommends you read " f"{post.title}"
            message = f"Read { post.title } at {post_url}\n\n" \
                      f"{cleaned['name']}\'s comments: {cleaned['comments']}"
            send_mail(subject, message, 'admin@bcuz.eu', [cleaned['to']])
            sent = True

    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html',
                  {'post': post,
                   'form': form,
                   'sent': sent,})
