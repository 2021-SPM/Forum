from django import forms

from .models import Post,Category

choices = Category.objects.all()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'category', 'header_image', 'author', 'body', 'emailNotice')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your title here'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'xxxa', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'emailNotice': forms.BooleanField(required=False)
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet','category','header_image', 'body', 'emailNotice')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your title here'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'emailNotice': forms.BooleanField()
        }

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type new catgory here'}),
        }