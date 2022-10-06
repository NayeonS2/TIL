from django import forms
from .models import Either, Comment


class EitherForm(forms.ModelForm):

    class Meta:
        model = Either
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('either',)