from django.db import models

class ContactModel(models.Model):
	full_name = models.CharField(max_length=50)
	phone_number = models.IntegerField()
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return "%s : %s" % (self.full_name, self.message[:20])


class AboutModel(models.Model):
	about_message = models.CharField(max_length=50)
	about_image = models.ImageField(upload_to='AboutImg')

	def __str__(self):
		return self.about_message[:50]