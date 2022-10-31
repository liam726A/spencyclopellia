from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('python', views.python_view, name='python'),
]