from django.contrib import admin
from .models import user_data, appdatabase, message, requested_app, BlogComment, Post

# Register your models here.
admin.site.register(user_data)
admin.site.register(appdatabase)
admin.site.register(requested_app)
admin.site.register(BlogComment)
admin.site.register(Post)
admin.site.register(message)
