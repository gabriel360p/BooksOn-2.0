from django.db import models

class tb_book(models.Model):
	title=models.CharField(max_length=30)
	author=models.CharField(max_length=30)
	price=models.CharField(max_length=30)
	categorie=models.CharField(max_length=30)
	text=models.TextField(max_length=255)
	def __str__(self):
	   return f'{self.title}, {self.author}, {self.title}, {self.price}, {self.categorie}'

# class tb_categories(models.Model):
# 	categorie=models.CharField(max_length=30)


class tb_user(models.Model):
	name=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	password=models.CharField(max_length=30)
	address=models.TextField(max_length=30)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	fk=models.ManyToManyField("tb_book")
	def __str__(self):
	   return f'{self.name}, {self.lastname}, {self.email}, {self.password}, {self.address},{self.city},{self.state}'