from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255) 
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=12)
    content = models.TextField()

    def __str__(self):
        return 'Sir You have got a message from ' + self.name 

