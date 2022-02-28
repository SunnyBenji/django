from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text
    # def publier(self):
    #    return self.date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.
