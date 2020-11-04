from django import forms
from everydayBlog.models import Post,Comments

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets= {
            'title':forms.textInput(attrs={'class': 'textinputclass'}),
            'text':forms.textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }





class CommentsForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ('author','text')

        widgets ={
            'author':forms.textInput(attrs={'class': 'textinputclass'}),
            'text':forms.textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
