




from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='classes'),
    path('<slug:category_slug>/<int:class_id>/', views.class_detail, name='class_detail'),
    path('categories/<slug : category_slug/', views.category_detail , name = 'classes_by_category'),
]
