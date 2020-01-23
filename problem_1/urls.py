from django.urls import path

from problem_1 import views

urlpatterns = [
    path('xl_calculation/', views.calculate_xl_data, name = 'calculation'),
]
