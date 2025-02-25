from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/news.html'  # Указан правильный путь к шаблону
    context_object_name = 'object_list'  # Соответствует шаблону
    ordering = '-published_at'  # Сортировка по дате публикации

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'  # Шаблон для детальной страницы
    context_object_name = 'article'
