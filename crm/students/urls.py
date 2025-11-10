from django.urls import path

from . import views

from twilio.rest import Client

urlpatterns = [

    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),

    path('students-list/',views.StudentListView.as_view(),name='students-list'),

    path('add-student/',views.AddStudent.as_view(),name='add-student'),

    path('students-details/<str:uuid>',views.StudentDetailsView.as_view(),name='student-details'),

    path('students-delete/<str:uuid>',views.StudentDeleteView.as_view(),name='student-delete'),

    path('student-edit/<str:uuid>',views.EditStudent.as_view(),name='student-edit'),


]

