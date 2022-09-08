from django.db import models

# Create your models here.
class City(models.Model):
	name_of_city = models.CharField(max_length=250)
	added_city = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name_of_city

	class Meta:
		ordering = ['-added_city']
