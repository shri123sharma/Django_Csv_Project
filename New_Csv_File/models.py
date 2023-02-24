from django.db import models
from django.contrib.auth.models  import User

class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=30)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=20)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PersonDetail(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female')
    )
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(verbose_name='display name',max_length=20,help_text='Name of the Person')
    gender = models.CharField(max_length=10,choices=GENDER)
    dob = models.DateField(auto_now=True)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    aadhaar = models.BigIntegerField()
    country = models.ForeignKey(Country,null=True,blank=True,on_delete=models.CASCADE)
    address = models.TextField()
    hobby = models.ForeignKey(Hobby,null=True,blank=True,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,null=True,blank=True,on_delete=models.CASCADE)
    internal_status = models.CharField(max_length=20,choices=(('active','Active'),('suspended','Suspended')),null=True,blank=True)
    status = models.IntegerField(default=1)
    creation_time = models.TimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.name,self.email)
