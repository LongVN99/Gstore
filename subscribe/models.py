from django.db import models

# Create your models here.

class Join(models.Model):
    email= models.EmailField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__ :
        return self.email