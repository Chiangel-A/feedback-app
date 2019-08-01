from django.db import models
from django.conf import settings

# Create your models here.

# Extension for user model
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=100)
	home_address = models.CharField(max_length=250, null=True)
	gender = models.CharField(max_length=100, null=True)
	


class Subject(models.Model):
	name = models.CharField(max_length=35)

	def __str__(self):

		return self.name


class Course(models.Model):
	name = models.CharField(max_length=200)
	facilitator = models.CharField(max_length=200, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	

	def __str__(self):

		return self.name


# Model for entreprenuership feedback form
class Entreprenuership(models.Model):
	course_title = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
	question_1 = models.TextField()
	question_2 = models.TextField()
	question_3 = models.TextField()
	question_4 = models.CharField(max_length=100)

# Model for ICT feedback form
class Ict(models.Model):
	course_title = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='title')
	question_1 = models.CharField(max_length=128)
	question_2 = models.CharField(max_length=128)
	question_3 = models.CharField(max_length=128)
	question_4 = models.CharField(max_length=128)
	question_5 = models.CharField(max_length=128)
	question_6 = models.CharField(max_length=128)
	question_7 = models.CharField(max_length=128)
	question_8 = models.TextField()
	question_9 = models.TextField()
	




	