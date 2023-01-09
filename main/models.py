from django.db import models

# Create your models here.
class Skill(models.Model):
    tittle = models.CharField(max_length=255)


class Message(models.Model):
        name = models.CharField(max_length=255,verbose_name='имя')
        email = models.EmailField('почта')
        text = models.TextField(verbose_name='сообщение')

class Project(models.Model):
    tittle = models.CharField(max_length=255)
    discription = models.TextField()
    link = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static')