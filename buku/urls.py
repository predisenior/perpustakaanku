from django.urls import path
from .views import BukuListView, BukuCreateView

urlpatterns = [

    path('',BukuListView.as_view(),name='home'),
    path('new/',BukuCreateView.as_view(),name='new'),
]