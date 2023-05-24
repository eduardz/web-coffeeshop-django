from django.db import models

# https://stackoverflow.com/questions/60926171/i-cant-make-the-image-url-to-load-on-local-host-please-hlp
class Coffee(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(default=10)
    image_url = models.CharField(max_length=2083)

