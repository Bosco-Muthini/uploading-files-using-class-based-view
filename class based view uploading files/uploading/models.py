from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')
    cover=models.ImageField(upload_to='books/covers', null=False,blank=False)

    def __str__(self):
        return self.title