from django.contrib import admin
from models import Entries,Category
admin.site.register(Entries)
admin.site.register(Category)
'''
class EntriesAdmin(admin.TabularInline):
	model = Entries
class CategoryAdmin(admin.ModelAdmin):
	inlines =[EntriesAdmin,]

admin.site.register(Entries)
admin.site.register(Category)
'''


# Register your models here.
