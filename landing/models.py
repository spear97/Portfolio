from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=300)
    percentage = models.BigIntegerField()

    def __str__(self):
         return f"{self.name} | {self.percentage}"