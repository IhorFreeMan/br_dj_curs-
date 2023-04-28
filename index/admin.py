from django.contrib import admin
from index.models import Category, Notes
# Register your models here.



@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title']


admin.site.register(Category)
# admin.site.register(Notes)