from django.contrib import admin
from .models import About , StudentReview

@admin.register(About)
class AboutAdmin (admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(StudentReview)
class StudentReviewAdmin(admin.ModelAdmin):
    list_display = ('name', ) 