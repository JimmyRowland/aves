from django import forms
from django.contrib.auth.models import User

from .models import Book, Chapter


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['writer', 'book_title', 'genre', 'book_cover']


class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ['chapter', 'transcriptVTT_file', 'YouTube_link']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


