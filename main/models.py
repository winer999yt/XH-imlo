from django.db import models

class Correct(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Incorrect(models.Model):
    word = models.CharField(max_length=50)
    correct = models.ForeignKey(Correct, on_delete=models.CASCADE)
    def __str__(self):
        return self.word

