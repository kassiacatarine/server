from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)