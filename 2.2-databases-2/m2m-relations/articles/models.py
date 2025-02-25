from django.db import models

# Модель тега
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название тега')  # Уникальное название тега

    def __str__(self):
        return self.name

# Модель статьи (обновленная)
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles', verbose_name='Теги')  # Связь через Scope

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']  # Сортировка статей по дате публикации (от новых к старым)

    def __str__(self):
        return self.title

# Промежуточная модель для связи статьи и тега
class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Тег')
    is_main = models.BooleanField(default=False, verbose_name='Основной тег')  # Является ли тег основным

    class Meta:
        unique_together = ('article', 'tag')  # Уникальность пары статья-тег
        ordering = ['-is_main', 'tag__name']  # Сортировка: основной тег первый, затем по имени тега
        verbose_name = 'Раздел статьи'
        verbose_name_plural = 'Разделы статей'

    def __str__(self):
        return f"{self.tag.name} ({'основной' if self.is_main else 'дополнительный'})"
