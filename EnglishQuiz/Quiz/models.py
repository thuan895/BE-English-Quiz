from typing import Text
from django.db import models
from django.db.models.fields import CharField

#1
class Exercise(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time = models.IntegerField(default=0)
    def __str__(self):
            return self.title
#2
class Question(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.IntegerField(default=0)
    def __str__(self):
            return self.description[:50]
#3
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField()
    is_correct = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    score_max = models.CharField(max_length=50, default="")
    national = models.CharField(max_length=50, default="")
    career = models.CharField(max_length=50, default="")
class Ranking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    score = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
class Pre_Exercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=50)
class Answer_done(models.Model):
    pre_exercise = models.ForeignKey(Pre_Exercise, on_delete=models.CASCADE)
    correct_ans = models.CharField(max_length=50)
    user_ans = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
class Base(models.Model):
    score_min=models.CharField(max_length=50)
    score_max=models.CharField(max_length=50)
    certificate=models.CharField(max_length=50)
    type=models.CharField(max_length=50)