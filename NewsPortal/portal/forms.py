from django import forms
from .models import Post, Category

class NewsForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Используем чекбоксы
        label='Категории'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class ArticleForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Используем тот же виджет
        label='Категории'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']