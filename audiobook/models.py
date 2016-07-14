from django.contrib.auth.models import Permission, User
from django.db import models

class Book(models.Model):
    user = models.ForeignKey(User, default=1)

    writer = models.CharField(max_length=250)
    book_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    book_cover = models.FileField()


    def __str__(self):
        return self.book_title + ' - ' + self.writer


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.IntegerField(default=1)
    transcriptVTT_file = models.FileField(default='')
    YouTube_link = models.CharField(max_length=500)
    YouTube_key = models.CharField(max_length=500)

    def __str__(self):
        return 'Chapter ' + str(self.chapter)