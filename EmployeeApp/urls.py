from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentApi, name='department-list'),
    path('department/<int:id>/', views.departmentApi, name='department-detail'),

    path('employee/', views.employeeApi, name='employee-list'),
    path('employee/<int:id>/', views.employeeApi, name='employee-detail'),

    path('employee/savefile/', views.SaveFile, name='save-file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
