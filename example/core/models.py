from django.db import models

# Create your models here.
class Contact(models.Model): 
    name=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    usertype=models.CharField(max_length=122)
    date= models.DateField()

class send_money(models.Model):
    name=models.CharField(max_length=122)
    amount=models.CharField(max_length=122)
    date= models.DateField()
    