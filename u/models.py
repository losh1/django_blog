from __future__ import unicode_literals

from django.db import models

class Author(models.Model):	
	'''
	define the blog_Author table
	'''
	name = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	bio = models.TextField()

	def __str__(self):
		return self.name

class Category(models.Model):
	cat_name = models.CharField('Category Name', max_length=50)
	cat_description = models.CharField('Category Description', max_length=255)

	class Meta:
		verbose_name_plural = 'Categories'


	def __str__(self):
		return self.cat_name

class Tag(models.Model):
	tag_name = models.CharField(max_length=50)
	tag_description = models.CharField(max_length=255)

	def __str__(self):
		return self.tag_name

class Post(models.Model):
	'''
	define blo_Post Table
	'''
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	author = models.ForeignKey(Author)
	category = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title


