from django.db import models

# Create your models here.
class Apply_contact(models.Model):
    name=models.CharField(max_length=200)
    mail=models.EmailField(max_length=300)
    subject=models.CharField(max_length=200)
    messages=models.TextField(max_length=800)

    class Meta:
        verbose_name=("Apply_contact")
        verbose_name_plural=("Apply_contacts")
    
    def __str__(self):
        return self.name
