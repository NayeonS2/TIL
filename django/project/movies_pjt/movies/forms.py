from dataclasses import field
from logging import PlaceHolder
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):


    class Meta:
        model = Movie
        exclude = ('user',)
        labels = {
            'title': 'Title',
            'audience': 'Audience',
            'release_date': 'Release date',
            'genre': 'Genre',
            'score': 'Score',
            'poster_url': 'Poster url',
            'description': 'Description',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class':'form-control'}),
            'audience': forms.NumberInput(attrs={'placeholder':'Audience','class':'form-control'}),
            'release_date': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'placeholder':'연도-월-일', 'type':'date','class':'form-control'
            }),
            'genre': forms.Select(attrs={'placeholder': '코미디','class':'form-control'}),
            'score': forms.NumberInput(attrs = {
                'step': 0.5,
                'min' : 0,
                'max' : 5,
                'class':'form-control',
                'placeholder': 'Score'

                }
            ),
            'poster_url': forms.Textarea(attrs={'placeholder': 'Poster url','class':'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description','class':'form-control'}),

        }
        