from django.contrib import admin
from django.urls import path,include
from problem_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('problem/', include('problem_1.urls')),
    path('xl_solutions/', views.Home.as_view(), name = 'home'),
]
