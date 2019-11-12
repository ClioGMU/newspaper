from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleRebuttalView

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("rebuttal/<int:pk>/", ArticleRebuttalView.as_view(), name="article_rebuttal"),
]
