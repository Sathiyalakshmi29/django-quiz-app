from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),
    path('submit/', views.submit, name='submit'),
]