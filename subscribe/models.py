from django.db import models

# Create your models here.

class SubscribeUser(models.Model):
    email = models.EmailField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email