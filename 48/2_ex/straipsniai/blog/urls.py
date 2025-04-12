from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, \
    ArticleDeleteView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/naujas/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/redaguoti/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/istrinti/', ArticleDeleteView.as_view(), name='article_delete'),
]
