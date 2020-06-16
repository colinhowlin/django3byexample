"""Defines the apps views"""

from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm

"""
def post_list(request):
    #View showing list of blog entries

    # retrieve all published posts
    object_list = Post.published.all()
    # Instantiate Paginator with published posts, 3 posts per page
    paginator = Paginator(object_list, 5)
    # Get the current page number
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, show the last page
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})
"""

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

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields pass validation
            cd = form.cleaned_data

            # ToDo: send email

    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html',
                  {'post': post,
                   'form': form})
