from django.db import models

# Create your models here.

class registration_table(models.Model):
    user_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name  

class contact_table(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=200)   

    def __str__(self):
        return self.name

class add_customer_table(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)

    def __str__(self):
        return self.name        
