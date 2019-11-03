# -*- coding: utf-8 -*-

from django.db import models


# Model with examples fields
class ExampleModel1(models.Model):
	bigiintagerfield = models.BigIntegerField(default=0)
	binaryfield = models.BinaryField(max_length=100, default=b'\xf0\xf1\xf2')
	booleanfield = models.BooleanField(null=True)
	charfield = models.CharField(max_length=100, default=None)
	

class ExampleModel2(models.Model):
	datefield = models.DateField(auto_now_add=True, null=True, blank=True)
	datetimefield = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	decimalfield = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	durationfield = models.DurationField(null=True)
	emailfield = models.EmailField(max_length = 254, null=True)
	

class ExampleModel3(models.Model):		
	filefield = models.FileField(upload_to='uploads/', null=True)
	filepathfield = models.FilePathField(path=None, match=None, max_length=200, null=True)
	floatfield = models.FloatField(default=0)
	imagefield = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100, null=True)
	integerfield = models.IntegerField(default=0)

class ExampleModel4(models.Model):
	genericipaddressfield = models.GenericIPAddressField(protocol='IPv4', null=True)
	nullbooleanfield = models.NullBooleanField()
	positiveintegerfield = models.PositiveIntegerField(default=0)
	positivesmallintegerfield = models.PositiveSmallIntegerField(default=0)
	slugfield = models.SlugField(max_length=100, allow_unicode=True)

class ExampleModel5(models.Model):
	smallintegerfield = models.SmallIntegerField(default=0)
	textfield = models.TextField()
	timefield = models.TimeField(auto_now_add=False, auto_now=False)
	urlfield = models.URLField(max_length=200)
	uuidfield = models.UUIDField(primary_key=True, default=1, editable=False)