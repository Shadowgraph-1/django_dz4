from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'articles'  # Обновлено с 'news' на 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),  # Список статей (использует news.html)
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),  # Детальная страница статьи
]