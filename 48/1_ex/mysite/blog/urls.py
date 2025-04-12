from django.urls import path
from .views import PostListView, PostDetailView, PostCreatView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('naujas/', PostCreatView.as_view(), name='post_create'),
    path('<int:pk>/redaguoti/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/istrinti/', PostDeleteView.as_view(), name='post_delete'),
]