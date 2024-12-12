from django.contrib import admin
from .models import UserProfile, Poem, Comment

admin.site.register(UserProfile)
admin.site.register(Poem)
admin.site.register(Comment)
