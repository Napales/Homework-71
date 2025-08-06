from django import forms

from webapp.models import Post


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]
