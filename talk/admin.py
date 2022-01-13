from django.contrib import admin

# Register your models here.
from talk.models import Post, Answer

admin.site.register(Post)
admin.site.register(Answer)