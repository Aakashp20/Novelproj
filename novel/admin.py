from django.contrib import admin
from .models import UserTypeMaster, UserMaster, BookMaster, CategoryMaster, ChapterMaster

# # Register your models here.

ModelField=lambda model: type('SubClass'+model.__name__,(admin.ModelAdmin,),{
	'list_display':[x.name for x in model._meta.fields],
	})
admin.site.register(UserMaster,ModelField(UserMaster))
admin.site.register(UserTypeMaster,ModelField(UserTypeMaster))
admin.site.register(CategoryMaster,ModelField(CategoryMaster))
admin.site.register(BookMaster,ModelField(BookMaster))
admin.site.register(ChapterMaster,ModelField(ChapterMaster))


