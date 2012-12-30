from django.db import models

class Books(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=100)
	read = models.CharField(max_length=3)
	
	def __unicode__(self):
		return self.title + " / " + self.author + " / " + self.read