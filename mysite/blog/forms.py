from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        return content

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
