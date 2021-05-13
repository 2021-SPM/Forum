from django.urls import path

from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, CategoryView, \
    AddCatView, search

app_name = 'myblog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',
         ArticleDetailView.as_view(),
         name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),
         name='update_post'),
    path('article/<int:pk>/delete',
         DeletePostView.as_view(),
         name='delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('cats/<int:pk>', CategoryView.as_view(), name='cats'),
    path('add_cat/', AddCatView.as_view(), name='add_cat'),
    path('search/', search, name='search'),
]
