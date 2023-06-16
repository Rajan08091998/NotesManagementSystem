from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    note_type = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.title}'