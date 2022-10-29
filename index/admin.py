from django.contrib import admin
from .models import Category, Topic, Language, Library, Spell

# Register your models here.
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Language)
admin.site.register(Library)
admin.site.register(Spell)
