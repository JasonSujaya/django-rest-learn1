from django.db import models

# Create your models here.


class NotesTry1(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Comment1(models.Model):
    notes_id = models.ForeignKey(NotesTry1, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.content
