from django.urls import path, include
from rest_framework import routers
from courses import views


router = routers.DefaultRouter()
router.register('', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),

]
