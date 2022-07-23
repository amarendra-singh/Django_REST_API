# from functools import partial
# from django.shortcuts import render
# from itsdangerous import Serializer
# from requests import request
# from yaml import serialize

from requests import Session
from rest_framework.response import Response
# from rest_framework.decorators import APIView
from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer
from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .custompermission import MyPermissioin

#Auth & Permission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [MyPermissioin]
    # permission_classes = [IsAuthenticated]
    # permission_classes= [IsAdminUser]
    # permission_classes= [AllowAny]






    
#-------------------------------------------------------------------
#ModelView
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentROMViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#-------------------------------------------------------------------------

#Mixin


# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args, **kwargs)

# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update( request, *args, **kwargs)    

# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class LCSTudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class  = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def update(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


#ListAPIView

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer




# # @api_view(['POST'])
# # def hello_world(request):
# #     if request.method == 'POST':
# #         print(request.data)
# #         return Response ({'msg':'Hello world'})




# # @api_view(['GET','POST','PUT','PATCH','DELETE'])

# class StudentAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id =id)
#             serializer= StudentSerializer(stu)
#             return Response(serializer.data)

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Data Created"}, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None, format=None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializer(stu, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response ({"msg": "Complete Data has been updated"}, 
#             status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk = None, format = None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializer(stu, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"MSG": "Partial data updated"})
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk = None, format =None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response({"msg": "Record deleted"})
#--------------------------------------------------------------------------------------

#-------------------------------------------------------------------

# #ViewSet
# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk = None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
    
#     def create (self, request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Data Created"}, status = status.HTTP_201_CREATED)
#         return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"MSG": "Record has been updated"}, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializer(stu, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"MSG":"Partial record updated"})
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk):
#         id = pk
#         stu = Student.objects.get(pk =id)
#         stu.delete()
#         return Response({"MSG":"Record has been deleted"})



#-----------------------------------------------------------------------------------------