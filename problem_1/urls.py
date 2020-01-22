from django.urls import path

from problem_1 import views

urlpatterns = [
    path('solution/', views.Home.as_view(), name = 'home'),
]
