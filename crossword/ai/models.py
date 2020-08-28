from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=255)
    word_lenght = models.IntegerField()

    def __str__(self):
        return self.word

    class Meta:
        db_table = "dictionary"
