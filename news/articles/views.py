from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Article

class ArticleView(ListView):
    model = Article
    template_name = 'articles_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'

class ArticleDetaleView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')