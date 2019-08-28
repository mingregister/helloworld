
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='blog-index'), # it can not be write as '/'
    # path('<int:page>', views.BlogList.as_view(), name='blog-index'), 
    path('', views.BlogList.as_view(), name='blog-index'), # it can not be write as '/'
    path('post/', views.PostView.as_view(), name='blog-post'), 
    path('comment/<int:blogid>/', views.CommentView.as_view(), name='blog-comment'), 
    path('search/', views.SearchView.as_view(), name='blog-search'), 
    path('follow/', views.FollowView.as_view(), name='blog-follow'), 
]
