from django.db import models

# Create your models here.

class Admin(models.Model):
	product_name=models.CharField(max_length=200)
	product_price=models.PositiveIntegerField()
	product_image=models.ImageField(upload_to='product_pic')
	product_model=models.CharField(max_length=200)


	def __str__(self):
		return  self.product_name