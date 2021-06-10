from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category', 'tags']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def save(self):
        data = self.cleaned_data
        data['author'] = self.request.user
        tags = data.pop('tags')
        post = Post.objects.create(**data)
        post.tags.add(*tags)
        return post

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category', 'tags']

