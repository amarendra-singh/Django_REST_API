from api import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken

#Creating Ruoter Object
router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename= 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework' )),
    path('gettoken/', CustomAuthToken.as_view())
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentListCreate.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.RUDStudentAPI.as_view())
]
