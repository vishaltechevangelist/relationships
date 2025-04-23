from django.urls import path
from fileuploads import views

urlpatterns = [
    path('home/', views.home)
]
