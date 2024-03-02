
from django.shortcuts import render
from .models import About , StudentReview

def about_view(request):
    abouts = About.objects.all()
    student_reviews = StudentReview.objects.all()

    context = {
        'abouts' : abouts,
        'student_reviews': student_reviews
    }
    return render(request, 'about.html', context)