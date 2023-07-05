from django.db import models

# Create your models here.

class Question(models.Model):
    question_name = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

class Choice(models.Model):
    your_choice = models.CharField(max_length=200)
   

   
