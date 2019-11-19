from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleRebuttalView,
    ArticleCreateView,
    ArticleUpdateView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("edit/<int:pk>", ArticleUpdateView.as_view(), name="article_edit"),
    path("rebuttal/<int:pk>/", ArticleRebuttalView.as_view(), name="article_rebuttal"),
]
