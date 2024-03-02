from django.contrib import admin
from .models import Class_obj , Category , Tag



@admin.register(Class_obj)
class Class_objAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}


@admin.register(Tag)
class TagAdmin (admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}