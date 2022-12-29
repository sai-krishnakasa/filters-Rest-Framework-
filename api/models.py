from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_no=models.CharField(max_length=6)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name