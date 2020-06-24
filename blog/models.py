"""This module defines the apps models"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Custom model manager for querying published posts
class PublishedManager(models.Manager):
    """Custom model manager to manage published posts"""
    def get_queryset(self):
        """Returns queryset of published posts"""
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """Defines the fields for blog posts"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    # The default model manager - must add this in addition to custom manager
    # if you want access to it
    objects = models.Manager()
    # Custom model manager for published posts
    published = PublishedManager()

    def get_absolute_url(self):
        """Returns the absolute URL of the blog post"""
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    # Inner class to hold Meta data
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Model for comments on blog posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
