from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Sual mətni")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Dərc tarixi")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200, verbose_name="Cavab variantı")
    votes = models.IntegerField(default=0, verbose_name="Səs sayı")

    def __str__(self):
        return self.choice_text