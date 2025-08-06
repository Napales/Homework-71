from django.urls import path

from webapp.views.posts import PostsListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = "webapp"

urlpatterns = [
    path('', PostsListView.as_view(), name="posts_list"),
    path('posts/add/', PostCreateView.as_view(), name="post_add"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_view"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
]
