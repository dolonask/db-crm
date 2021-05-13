from django.urls import path
from . import views

urlpatterns = [
    # path('source/', create_source, name='CreateSource'),
    path('', views.index, name='index'),
]
