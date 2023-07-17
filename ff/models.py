from django.db import models

# Create your models here.



class croprecomend(models.Model):
	soil=models.CharField(max_length=30)
	season=models.CharField(max_length=20)
	crop=models.CharField(max_length=100)
	image=models.ImageField(null=True,blank=True,upload_to="images/")
	class Meta:
		db_table="croprecomend"




    	


	