#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from models import Entries,Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import jieba
import jieba.analyse
import re
from django.utils.html import strip_tags

# Create your views here.
def hello(request):
	context={}
	return render(request, 'icms/index.html', context)
	#return HttpResponse('hello')
	

def index(request,page_num=1):
	PAGE_RECORDER=10
	entries_all=Entries.objects.all().filter(orderby__gte=0).order_by('-id')
	tags_all=[e.tags for e in entries_all]
	tags_all=','.join(tags_all)
	tags_all=tags_all.split(',')
	tags_all=set(tags_all)
	paginator =Paginator(entries_all,PAGE_RECORDER)
	try:
		entries_list=paginator.page(page_num)
	except PageNotAnInteger:
		entries_list=paginator.page(1)
	except EmptyPage:
		entries_list=paginator.page(paginator.num_pages)
	context={'entries_list':entries_list,'tags_all':tags_all}
	return render(request, 'icms/index.html', context)
	
def entries_views(request,entries_id):
	entries=Entries.objects.filter(orderby__gte=0).get(pk=entries_id)
	#jieba.set_dictionary("/home/app/django_projects/leecms/icms/mysite/jieba.txt")
	#jieba.initialize()
	#删除html标签,方便抽取关键词
	#dr=re.compile(r'<[^>]+>',re.S)
	#keywords=jieba.analyse.extract_tags(dr.sub('',entries.content),5)
	keywords=jieba.analyse.extract_tags(strip_tags(entries.content),5)
	context={'entries':entries,'keywords':keywords}
	return render(request,'icms/entries.html',context)
	

def category_views(request,page_num):
	PAGE_RECORDER=10
	entries_all=Entries.objects.all().filter(orderby__gte=0).order_by('-id')
	paginator =Paginator(entries_all,PAGE_RECORDER)
	
	try:
		entries_list=paginator.page(page_num)
	except PageNotAnInteger:
		entries_list=paginator.page(1)
	except EmptyPage:
		entries_list=paginator.page(paginator.num_pages)
	context={'entries_list':entries_list}
	return render(request, 'icms/category.html', context)
