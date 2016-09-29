from django.db import models
from django.contrib.auth.models import User


def upload_path_handler(instance, filename):
	suffix = filename.split('.')[-1]
	filename = str(instance.user.username) +  '_.' + suffix
	return "users/%Y/%m/%d/{}".format(filename)  # Ymd invalid


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	nickname = models.CharField(max_length=20, blank=True)
	phone = models.CharField(max_length=11, blank=True)
	website = models.URLField(blank=True)
	birthday = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', default="users/default.png")


	def __str__(self):
		return "{}'s UserProfile".format(self.user.username)


class SocialUser(models.Model):
	choices = (
		('GH', 'github'),
		('WX', 'weixin'),
		('QQ', 'qq'),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_user')
	
	login = models.CharField(max_length=50)
	social_id = models.IntegerField()

	belong = models.CharField(max_length=10, choices=choices)

	def __str__(self):
		return "{}-{}".format(self.belong, self.login)

	class Meta:
		ordering = ['belong', 'login']