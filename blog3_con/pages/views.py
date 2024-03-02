from django.shortcuts import render
from django.views.generic.edit  import FormView
from. forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    return render(request, 'index.html' )


# def about(request):
#     return render(request, 'about.html' )




from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})