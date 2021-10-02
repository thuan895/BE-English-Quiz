from Quiz.views import *
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string
from Quiz.firebasechild import datachild
from django.forms.models import model_to_dict

#########################################
@receiver(post_save, sender=Exercise)
def create_exercise(sender, instance, created, **kwargs):
    if created:
        print("createExercise+++++++++++++++++++++")
        write_without_date('Exercise',instance)

@receiver(post_save, sender=Exercise)
def save_exercise(sender, instance, **kwargs):
    print("saveExercise------------------------")
    write_without_date('Exercise',instance)
#########################################
@receiver(post_save, sender=Question)
def create_question(sender, instance, created, **kwargs):
    if created:
        print("createQuestion+++++++++++++++++++++")
        write_without_date('Question',instance)

@receiver(post_save, sender=Question)
def save_question(sender, instance, **kwargs):
    print("saveQuestion------------------------")
    write_without_date('Question',instance)
#########################################
@receiver(post_save, sender=Answer)
def create_answer(sender, instance, created, **kwargs):
    if created:
        print("createAnswer+++++++++++++++++++++")
        write_without_date('Answer',instance)

@receiver(post_save, sender=Answer)
def save_answer(sender, instance, **kwargs):
    print("saveAnswer------------------------")
    write_without_date('Answer',instance)


def write_without_date(fb_tbl,value):
    i= model_to_dict(value)
    database.child(datachild).child(fb_tbl).child(i['id']).set(i)