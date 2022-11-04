from django import forms
from .models import Review, Comment, ReComment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user',]

class ReCommentForm(forms.ModelForm):

    class Meta:
        model = ReComment
        fields = ('body', 'comment')
