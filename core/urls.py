from django.urls import path
from core import views

urlpatterns = [
    # home
    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),

]
