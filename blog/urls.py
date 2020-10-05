
from django.urls import path,re_path
#rom.import views
from .views import HomeView , ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView
from . import views


urlpatterns = [
    #path('', views.home,name='home'),
    path('',HomeView.as_view(),name="home"),
    path('article_detail/<int:pk>',ArticleDetailView.as_view(),name='article_details'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('article_detail/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article_detail/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView, name='like_post'),
]