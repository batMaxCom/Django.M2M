from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_list = [form.cleaned_data['is_main'] for form in self.forms if form.cleaned_data]
        if main_list.count(True) > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif main_list.count(True) == 0:
            raise ValidationError('Должен быть выбран основной раздел')

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 4
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
