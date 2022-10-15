from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    """
    model for question
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    date_create = models.DateTimeField()
    date_modify = models.DateTimeField(null=True, blank=True)  # null is for DB, blank is for validation

    def __str__(self):
        return self.subject


class Answer(models.Model):
    """
    model for answer
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    date_create = models.DateTimeField()
    date_modify = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content