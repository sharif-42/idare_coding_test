from django.contrib import admin
from django.urls import path,include
from problem_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('problem_1.urls')),
]
