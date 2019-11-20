from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView
from . import views


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    # path('new/', views.newPage, name='newPage'),
    path('new/', PageCreateView.as_view(), name='newPage'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    
]
