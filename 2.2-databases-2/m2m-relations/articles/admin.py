from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope

# Формсет для проверки наличия ровно одного основного тега
class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_count = 0
        # Подсчитываем количество основных тегов
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_main'):
                    main_count += 1
        # Проверка: должен быть ровно один основной тег
        if main_count != 1:
            raise ValidationError('Должен быть ровно один основной тег.')

# Inline для редактирования связей Scope
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1  # Одна пустая строка для добавления тега

# Админка для статьи
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]  # Подключаем управление тегами
    list_display = ('title', 'published_at')  # Показывать название и дату публикации
    search_fields = ('title', 'text')  # Поиск по названию и тексту

# Админка для тега
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Показывать только название тега
    search_fields = ('name',)  # Поиск по названию тега