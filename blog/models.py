from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

		def __str__(self):
			return self.title

'''
- models.Model means that the Post is a Django Model, so Django knows   that it should be saved in the database.
- models.ForeignKey: this is a link to another model.

'''