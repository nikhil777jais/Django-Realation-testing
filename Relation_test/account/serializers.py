from rest_framework import serializers
from . models import Teacher, Student
from django.contrib.auth import get_user_model
User = get_user_model()


#employee serialiser
class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['id','name','phone',]
 
  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.phone = validated_data.get('phone', instance.phone)
    instance.save()
    return instance     
    
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id','name','phone',]

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.phone = validated_data.get('phone', instance.phone)
    instance.save()
    return instance    

#user serialiser
class TeacherSignUpSerializer(serializers.ModelSerializer):
  teacher_detail = TeacherSerializer(many=False, read_only=False) 
  class Meta:
    model = User
    fields = ['email','password','profile','teacher_detail']  

  def create(self, validated_data):
    teacher_data = validated_data.pop('teacher_detail')
    user = User.objects.create(email=validated_data['email'])
    user.groups.add(1)
    user.profile = validated_data['profile']
    user.set_password(validated_data['password'])
    user.save()
    Teacher.objects.create(user=user, **teacher_data)
    return user 

  def update(self, instance, validated_data):
    teacher_data = validated_data.pop('teacher_detail')
    instance.email = validated_data.get('email', instance.email)
    instance.set_password(validated_data.get('password', instance.password))
    instance.profile = validated_data.get('profile', instance.profile)
    instance.save()
    Teacher.objects.update(**teacher_data)
    return instance    

class StudentSignUpSerializer(serializers.ModelSerializer):
  student_detail = StudentSerializer(many=False, read_only=False) 
  class Meta:
    model = User
    fields = ['email','password','profile','student_detail']

  def create(self, validated_data):
    student_data = validated_data.pop('student_detail')
    user = User.objects.create(email=validated_data['email'])
    user.groups.add(2)
    user.profile = validated_data['profile']
    user.set_password(validated_data['password'])
    user.save()
    Student.objects.create(user=user, **student_data)
    return user 

  def update(self, instance, validated_data):
    student_data = validated_data.pop('student_detail')
    instance.email = validated_data.get('email', instance.email)
    instance.set_password(validated_data.get('password', instance.password))
    instance.profile = validated_data.get('profile', instance.profile)
    instance.save()
    Student.objects.update(**student_data)
    return instance