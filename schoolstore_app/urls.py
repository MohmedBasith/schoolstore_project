from django.contrib import admin
from django.urls import path, include
from schoolstore_app import views
app_name = 'schoolstore_app'

urlpatterns = [
    path('', views.allCourse, name='allCourse'),
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/form/', views.form, name='form'),
    path('submit/', views.submit, name='submit'),
    # path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
    # path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path("load_courses/", views.load_courses, name="load_courses"),
    path('<slug:c_slug>/', views.allCourse, name='courses_by_category'),
    path('<slug:c_slug>/<slug:course_slug>/', views.courseDetail, name='crsdptdetail'),
]