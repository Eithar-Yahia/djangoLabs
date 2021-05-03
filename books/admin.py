from django.contrib import admin

from .models import Book, Category, Metric, CopyRight

from .forms import BookForm

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    #to apply validation on forms which i made
    form = BookForm
    list_display = ("title", "author", "content")
    list_filter = ("categories", )
    search_fields = ("title", )


class BookInline(admin.StackedInline):
    model = Book
    max_num = 3
    extra  = 1

class CopyRightAdmin(admin.ModelAdmin):
    inlines = [BookInline]
admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Metric)
admin.site.register(CopyRight,CopyRightAdmin)


