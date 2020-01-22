from django.urls import path

from problem_1 import views

urlpatterns = [
    # path('get/', views.Get.as_view(), name = 'home'),
    # path('post/', views.Post.as_view(), name = 'post'),
    path('calculation/', views.post_edit, name = 'calculation'),
]
