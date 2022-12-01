from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('poke/', include('poke.urls')),
]
