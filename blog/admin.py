from django.contrib import admin

from .models import Post


# this decorator registers the class it decorates to the admin interface
# this is the same as admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display allows you to specify which fields to display in the object list page
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    # adds a sidebar to filter by the fields defined in list_filter
    list_filter = ('status', 'created', 'publish', 'author')

    # adds a search bar to the admin page to search by the fields in search_fields
    search_fields = ('title', 'body')

    # When adding a new post, as the title is typed, the slug is automatically filled
    prepopulated_fields = {'slug': ('title',)}

    # Allows lookup of author with a searchable dialog
    raw_id_fields = ('author',)

    # groups objects by date and allows navigation by date
    date_hierarchy = 'publish'

    # Order by status and date
    ordering = ('status', 'publish')

