from __future__ import unicode_literals

from django.db import models

class Color(models.Model):
	color = models.CharField(max_length=1000)
	colorIdentity = models.CharField(max_length=1)
	def __str__(self):
		return self.color

class SuperTypes(models.Model):
	supertype = models.CharField(max_length=1000)
	def __str__(self):
		return self.supertype

class Types(models.Model):
	type = models.CharField(max_length=1000)
	def __str__(self):
		return self.type

class SubTypes(models.Model):
	subtype = models.CharField(max_length=1000)
	def __str__(self):
		return self.subtype

class CardTraduction(models.Model):
	imageUrl = models.URLField(max_length=250)
	language = models.CharField(max_length=1000)
	text = models.TextField()
	cardId = models.IntegerField(null=False)

class CardU(models.Model):
	cardName = models.CharField(max_length=1000, null=True)
	mana = models.CharField(max_length=1000, null=True)
	text = models.TextField()
	cmc = models.IntegerField(default=0)
	colors = models.ManyToManyField(Color, null=True, related_name='cardUs')
	typeCard = models.CharField(max_length=1000,null=True)
	"""supertypes = models.ManyToManyField(SuperTypes)"""
	types = models.ManyToManyField(Types)
	"""subtypes = models.ManyToManyField(SubTypes)"""
	rarity = models.CharField(max_length=100,null=True)
	power = models.CharField(max_length=100, null=True)
	multiverseid = models.IntegerField(default=0)
	number = models.CharField(max_length=1000, null=True)
	imageUrl = models.URLField(max_length=250, null=True)
	traduction = models.IntegerField(null=True)
	def __str__(self):
		return self.cardName