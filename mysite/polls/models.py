import datetime

from django.db import models
from django.utils import timezone

class Questionnaire(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    create_user_id = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_user_id = models.IntegerField()
    update_date = models.DateTimeField(auto_now=True)

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    questionnaire_id = models.IntegerField()
    question = models.CharField(max_length=1024)

class Choice(models.Model):
    id = models.IntegerField(primary_key=True)
    questionnaire_id = models.IntegerField()
    question_id = models.IntegerField()
    number = models.IntegerField()
    text = models.CharField(max_length=256)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    questionnaire_id = models.IntegerField()
    question_id = models.IntegerField()
    answerer_name = models.CharField(max_length=64)
    answerer_ip = models.CharField(max_length=64)
    create_date = models.DateTimeField(auto_now_add=True)

class AnswerDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    questionnaire_id = models.IntegerField()
    answer_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.IntegerField()


