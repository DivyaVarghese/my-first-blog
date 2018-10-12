from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image 
# Create your models here.
	
class Register(models.Model):
	user1=models.ForeignKey(User,on_delete=models.CASCADE)
	country=models.CharField(max_length=200)


	def __str__(self):
		return self.country


class Postadd(models.Model):
	user1=models.ForeignKey(Register,on_delete=models.CASCADE)
	title=models.CharField(max_length=300)
	text=models.TextField()
	date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
	photo = models.ImageField(upload_to='pics', blank=True)


	def __str__(self):
		return self.title

class Postedit(models.Model):
	user1=models.ForeignKey(Postadd,on_delete=models.CASCADE)
	title=models.CharField(max_length=300)
	text=models.TextField()


	def __str__(self):
		return self.title
