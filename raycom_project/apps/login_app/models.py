from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registerVal(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="First Name must be at least 2 characters long"
        if len(postData['last_name'])<2:
            errors['last_name']="Last Name must be at least 2 characters long"
        if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
            errors['alpha']="Name must contain only letters."
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            errors['email']="You must enter a valid email"
        if len(self.filter(email=postData['email'])) != 0:
            errors['emailexist']="Email already registered"
        if re.search('[0-9]',postData['password']) is None:
            errors['password_num']="Your password must contain at least one number"
        if re.search('[A-Z]',postData['password']) is None: 
            errors['password_cap']="Your password must contain at least one capital letter"
        if len(postData['password'])<8:
            errors['password_len']="Password must be at least 8 characters long"
        if postData['password'] != postData['c_password']:
            errors['password_val']="Password confirmation must match original password"
        if not postData['dob']:
            errors['dob']="You must enter a date of birth"
        return errors
    def createUser(self, postData):
        password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(
            first_name=postData['first_name'], 
            last_name=postData['last_name'],
            email=postData['email'],
            password=password,
            dob = postData['dob'],
            )
    def loginUser(self, postData):
        email_match=self.filter(email=postData['email'])
        print email_match
        errors={}
        if len(email_match) == 0:
            errors['email_match']="Email not found in database"
            return errors
        elif not bcrypt.checkpw(postData['password'].encode(), email_match[0].password.encode()):
            errors['password_match']="Password incorrect for email"
            return errors
        else:
            user=email_match[0]
            return user


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    dob = models.DateField()
    buddies = models.ManyToManyField('User', related_name="friends")
    objects=UserManager()


