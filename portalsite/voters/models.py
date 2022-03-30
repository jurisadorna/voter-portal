from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
class User(AbstractUser):
    is_admin=models.BooleanField('is admin',default=False)
    is_voter=models.BooleanField('is voter',default=False)
    is_faci=models.BooleanField('is facilitator',default=False)
    is_rep=models.BooleanField('is representative',default=False)
class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
class Voter(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mName=models.CharField(max_length=100)
    vId=models.CharField(max_length=100)
    pNum=models.CharField(max_length=100)
    Add=models.CharField(max_length=300)
    has_voted=models.BooleanField('Voted',default=False)
    contact=models.CharField(max_length=11, default='09000000000', validators=[RegexValidator(r'^[0-9]{11}$')])
class Rep(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mName=models.CharField(max_length=100)
    vId=models.CharField(max_length=100)
    pNum=models.CharField(max_length=100)
    Add=models.CharField(max_length=300)
    has_voted=models.BooleanField('Voted',default=False)
    contact=models.CharField(max_length=11, default='09000000000', validators=[RegexValidator(r'^[0-9]{11}$')])
class Faci(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
class Precinct(models.Model):
    pNum=models.CharField(max_length=100,unique=True)
    pAdd=models.CharField(max_length=300)
