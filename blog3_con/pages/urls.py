from . import views
from django.urls import path
from about import views as about_views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('about/', about_views.about_view, name='about'),
    path('contact/', views.contact , name = 'contact'),
]
