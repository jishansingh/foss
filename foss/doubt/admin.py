from django.contrib import admin
from .models import Question,Reply,UserProfile
# Register your models here.
admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(UserProfile)


