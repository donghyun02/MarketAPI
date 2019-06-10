from django.urls import path

from post import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('post/<int:post_id>/', views.PostRetrieveView.as_view()),
    path('comments/', views.CommentsView.as_view()),
]