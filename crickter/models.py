from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL
class Msg(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	msg = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name