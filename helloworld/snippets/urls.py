# -*- coding:utf-8 -*- 

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

from rest_framework.routers import DefaultRouter



# # 1.没使用viewset之前的url
# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     # path('', views.snippet_list),
#     # path('<int:pk>', views.snippet_detail),
#     path('', views.api_root), 
#     path('list/', views.SnippetList.as_view(), name='snippet-list'), # 这个list是我自己加去的。
#     path('<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
# 
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<pk>/', views.UserDetail.as_view(), name='user-detail'),
# 
#     path('<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]
# 
# urlpatterns = format_suffix_patterns(urlpatterns)


# # 2.使用viewset，但是没有使用router的url
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# 
# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     # path('', views.snippet_list),
#     # path('<int:pk>', views.snippet_detail),
#     path('', api_root), 
#     path('list/', snippet_list, name='snippet-list'), # 看文档的时候注意了，这个'list/'是我自己加去的。
#     path('<int:pk>/', snippet_detail, name='snippet-detail'),
# 
#     path('users/', user_list, name='user-list'),
#     path('users/<pk>/', user_detail, name='user-detail'),
# 
#     path('<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
# ]
# 
# urlpatterns = format_suffix_patterns(urlpatterns)

# 3.使用viewset,router情况下的url
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
