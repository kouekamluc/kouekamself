from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technology_stack']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured', 'order']
    readonly_fields = ['created_at', 'updated_at']