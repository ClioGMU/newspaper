from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article
from .forms import CommentFormSet
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

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["comment_formset"] = CommentFormSet(self.request.POST)
        else:
            context["comment_formset"] = CommentFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context["comment_formset"]
        form.instance.author = self.request.user
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]


class ArticleRebuttalView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_rebuttal.html"
