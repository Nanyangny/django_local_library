from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book','status','borrower', 'due_back','id')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInline(admin.TabularInline):
    model = Book

# admin.site.register(Author)
# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines =[BookInline]


admin.site.register(Genre)
# admin.site.register(Book,BookAdmin)
# admin.site.register(BookInstance)
  

