from django.contrib import admin
from .models import UserPaperPreference, Paper

admin.site.register(UserPaperPreference)
admin.site.register(Paper)
# Register your models here.
