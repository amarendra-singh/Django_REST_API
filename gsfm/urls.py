from api import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#Creating Ruoter Object
router = DefaultRouter()
router.register('studentapi', views.StudentROMViewSet, basename= 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentListCreate.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.RUDStudentAPI.as_view())
    path('', include(router.urls)),
]
