from django.shortcuts import render
from .models import Class_obj , Category

def class_list(request):
    classes = Class_obj.objects.all().order_by('-date')
    context = {
        'classes': classes
    }
    return render(request, 'classes.html', context)

def class_detail(request, category_slug, class_id):
    class_obj = Class_obj.objects.get(category__slug=category_slug, id=class_id)
    context = {
        'class_obj': class_obj
    }
    return render(request, 'class_detail.html', context)



def category_detail(request, category_slug):
    classes = Class_obj.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()


    context = {
        'classes': classes,
        'categories': categories,
        
    }
    return render(request, 'classes.html', context)