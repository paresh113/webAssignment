from django.db import models

# Create your models here.


class MultiStepFormModel(models.Model):
    id = models.AutoField(primary_key = True)
    age = models.IntegerField(max_length=222)
    sex = models.CharField(max_length=222)
    temp = models.FloatField(max_length=222)




    def __str__(self):
        return self.id