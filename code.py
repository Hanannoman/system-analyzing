# setup_virtual_meeting.py

# models.py
from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meetings_created')

    def __str__(self):
        return self.title

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='participants')
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('member', 'Member'),
        ('guest', 'Guest')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.meeting.title} ({self.role})"


# serializers.py
from rest_framework import serializers

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


# views.py
from rest_framework import viewsets

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'meetings', MeetingViewSet)
router.register(r'participants', ParticipantViewSet)

api_urlpatterns = [
    path('', include(router.urls)),
]


# virtual_meeting_platform/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # تأكد أن ملف api/urls.py يحتوي على api_urlpatterns
]
# 1. إنشاء مجلد المشروع
# mkdir virtual_meeting_platform
# cd virtual_meeting_platform

# 2. إنشاء بيئة افتراضية
# python -m venv venv
# source venv/bin/activate  # في ويندوز: venv\Scripts\activate

# 3. تثبيت Django و DRF
# pip install django djangorestframework


# 2: إنشاء مشروع وتطبيق

# 1. إنشاء مشروع Django
# django-admin startproject virtual_meeting_platform .

# 2. إنشاء تطبيق API
# python manage.py startapp api

# 3: تعديل settings.py

# افتح الملف: virtual_meeting_platform/settings.py

# 1. أضف 'rest_framework' و 'api' إلى INSTALLED_APPS:



# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'api',
# ]


# 4: إنشاء النماذج (models.py داخل app api)

# from django.db import models
# from django.contrib.auth.models import User

# class Meeting(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meetings_created')

# class Participant(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='participants')
#     role = models.CharField(max_length=50, choices=[
#         ('admin', 'Admin'),
#         ('manager', 'Manager'),
#         ('member', 'Member'),
#         ('guest', 'Guest')
#     ])


# 5: إنشاء Serializers (serializers.py)

# from rest_framework import serializers
# from .models import Meeting, Participant

# class MeetingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meeting
#         fields = 'all'

# class ParticipantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Participant
#         fields = 'all'


# الخطوة 6: إنشاء Views (views.py)

# from rest_framework import viewsets
# from .models import Meeting, Participant
# from .serializers import MeetingSerializer, ParticipantSerializer

# class MeetingViewSet(viewsets.ModelViewSet):
#     queryset = Meeting.objects.all()
#     serializer_class = MeetingSerializer

# class ParticipantViewSet(viewsets.ModelViewSet):
#     queryset = Participant.objects.all()
#     serializer_class = ParticipantSerializer


# 7: إعداد روابط التطبيق (api/urls.py)

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import MeetingViewSet, ParticipantViewSet

# router = DefaultRouter()
# router.register(r'meetings', MeetingViewSet)
# router.register(r'participants', ParticipantViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


# 8: إعداد روابط المشروع (virtual_meeting_platform/urls.py)

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),
# ]


# 9: التهيئة وتشغيل المشروع

# إنشاء قاعدة البيانات
# python manage.py makemigrations
# python manage.py migrate

# إنشاء مستخدم admin (اختياري)
# python manage.py createsuperuser

# تشغيل الخادم المحلي
# python manage.py runserver

# الآن يمكنك الدخول على:

# http://127.0.0.1:8000/api/meetings/
# http://127.0.0.1:8000/api/participants/