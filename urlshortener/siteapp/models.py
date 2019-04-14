from django.db import models

# Create your models here.
class Urls(models.Model):
	short_id = models.SlugField(max_length=8, primary_key=True)
	long_url = models.URLField(max_length=255)

	def __str__(self):
		return self.long_url
