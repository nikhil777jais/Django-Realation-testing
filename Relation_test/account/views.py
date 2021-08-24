from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeacherSignUpSerializer, TeacherSerializer, StudentSerializer, StudentSignUpSerializer
from django.shortcuts import get_object_or_404
from .models import Teacher, Student
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()
# Create your views here.

class TeacherSignUpAPI(APIView):
  def post(self, request, format = None):
    request.data['profile'] = 'teacher'
    serializer = TeacherSignUpSerializer(data=request.data) #request.data conatain the data that come from post request
    if serializer.is_valid():
      serializer.save()
      user = User.objects.get(email= serializer.data['email']) #get newly generated user
      refresh = RefreshToken.for_user(user) #generate a token for user just while signup
      return Response({'payload': serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token),'msg':'Data Saved!!',}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentSignUpAPI(APIView):
  def post(self, request, format = None):
    request.data['profile'] = 'student'
    serializer = StudentSignUpSerializer(data=request.data) #request.data conatain the data that come from post request
    if serializer.is_valid():
      serializer.save()
      user = User.objects.get(email= serializer.data['email']) #get newly generated user
      refresh = RefreshToken.for_user(user) #generate a token for user just while signup
      return Response({'payload': serializer.data,'refresh': str(refresh), 'access': str(refresh.access_token),'msg':'Data Saved!!',}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
    
class StudentAPI(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [DjangoModelPermissions]
  queryset = User.objects.none()
  def get(self, request, format=None):
    user = User.objects.get(email = request.data['email']) #the user who is currently loggedIn
    if user.profile == 'student':
      student_obj = Student.objects.get(user=user.id) #getting Student data realted to that user
      serializer = StudentSerializer(student_obj)
      return Response({'payload': serializer.data, 'msg':'Data Retrived!!'}, status = status.HTTP_200_OK)
    return Response({'msg':'only Student can access!!'}, status = status.HTTP_400_BAD_REQUEST)     

class TecherAPI(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [DjangoModelPermissions]
  queryset = User.objects.none()

  def get(self, request, id=None, format=None):
    user = User.objects.get(email = request.data['email']) #the user who is currently loggedIn
    if user.profile == 'student':
      return Response({'msg':'only Teacher can access!!'}, status = status.HTTP_400_BAD_REQUEST)
    # teacher_obj = Teacher.objects.get(user=user.id)
    # serializer_t = TeacherSerializer(teacher_obj)
    if not id == None:
      user_obj = Teacher.objects.get(pk=id)
      serializer = TeacherSerializer(user_obj)
      return Response({'payload': serializer.data, 'msg':'Data Retrived!!'},status = status.HTTP_200_OK)
    user_obj = Teacher.objects.all()
    serializer = TeacherSerializer(user_obj, many= True)
    return Response({'payload': serializer.data, 'msg':'Data Retrived!!'}, status = status.HTTP_200_OK)

  def post(self, request, format=None):
    serializer = TeacherSerializer(data=request.data) #request.data conatain the data that come from post request
    if serializer.is_valid():
      serializer.save()
      return Response({'payload': serializer.data,'msg':'Data Saved!!',}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  

  def patch(self, request, id = None, format = None):
    user_obj = Teacher.objects.get(pk=id)
    serializer = TeacherSerializer(user_obj, data = request.data, partial = True) #request.data get data from user ins
    if serializer.is_valid():
      serializer.save()
      return Response({'payload': serializer.data, 'msg':'Data Upadted Patially!!'}, status = status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

