from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='profile',null=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class DeletedCard(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='deleted_cards/')

    def __str__(self):
        return self.title