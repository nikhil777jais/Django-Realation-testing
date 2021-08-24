from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('ts/', views.TeacherSignUpAPI.as_view(), name='ts' ),#teacher sign-up
    path('ss/', views.StudentSignUpAPI.as_view(), name='ss' ),#student sign-up
    path('t/', views.TecherAPI.as_view(), name='t' ), #teacher view
    path('t/<int:id>/', views.TecherAPI.as_view(), name='tid' ),#teacher view
    path('s/', views.StudentAPI.as_view(), name='s' ), #student view
    path('gettoken/', jwt_views.TokenObtainPairView.as_view(), name='gettoken'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh')
]
