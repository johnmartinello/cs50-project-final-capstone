from django.contrib import admin
from .models import User, Course, Grade, Post, Forum, Assignment

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Assignment)


