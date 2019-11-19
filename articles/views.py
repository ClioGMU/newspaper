from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    ordering = ["-date"]


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]


class ArticleRebuttalView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_rebuttal.html"
