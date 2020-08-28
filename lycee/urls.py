from django.conf.urls import url
from . import views
from .views import StudentCreateView, particularcallView, edit_student
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>[0-9]+)$', views.cusus_student, name='cusus_student'),
    url(r'^cursuscall/(?P<student_id>[0-9]+)$', views.cusus_call, name='cursus_call'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^call/$', particularcallView.as_view(), name='particular_call'),
    path('student/edit/<int:pk>/', edit_student, name='edit_student'),
]