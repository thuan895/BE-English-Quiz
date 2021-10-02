from django.db import models

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