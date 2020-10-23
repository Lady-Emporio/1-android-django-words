from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(RelateGuidId)

class WordAdmin(admin.ModelAdmin):
	list_display = ("id","eng","ru")
	list_display_link = ("id")
	search_fields = ("eng","ru")

admin.site.register(Word,WordAdmin)
