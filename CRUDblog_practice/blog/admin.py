from django.contrib import admin
from .models import Post #내가 만든 포스트 클래스를 데려옴

admin.site.register(Post)
