from django.views.generic import ListView, DetailView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    ordering = ["-date"]


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleRebuttalView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_rebuttal.html"
