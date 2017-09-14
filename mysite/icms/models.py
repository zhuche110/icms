#coding=utf8
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from DjangoUeditor.models import UEditorField

from django.db import models

# Create your models here.

class Category(models.Model):
	name=models.CharField('栏目名', max_length=100)
	desc=models.TextField('描述',max_length=400,blank=True)
	orderby=models.IntegerField('排序',default=0)
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = ('栏目分类')
		verbose_name_plural = '栏目分类'


class Entries(models.Model):
	title=models.CharField('文章标题', max_length=100)
	content=RichTextUploadingField('文章内容', max_length=60000)
	author=models.CharField('作者', max_length=100,blank=True)
	orderby=models.IntegerField('排序',default=0)
	category=models.ForeignKey(
        		Category, verbose_name="栏目", default=1)
	tags=models.CharField('标签', max_length=400,blank=True)
	source=models.CharField('来源', max_length=100,default='原创')
	create_date = models.DateTimeField('创建日期',auto_now_add=True)
	update_date = models.DateTimeField('修改日期',auto_now=True)
	
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = ('文章')
		verbose_name_plural = '文章'



		
	
