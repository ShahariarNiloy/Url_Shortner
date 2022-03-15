from django.db import models
from hashlib import md5
# Create your models here.


class Url(models.Model):
    long_url = models.CharField(unique=True, max_length=1000)
    short_url = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.long_url

    @classmethod
    def create(self, long_url):
        temp_url = md5(long_url.encode()).hexdigest()[:5]

        try:
            obj = self.objects.create(long_url=long_url, short_url=temp_url)

        except:
            obj = self.objects.get(long_url=long_url)

        return obj
