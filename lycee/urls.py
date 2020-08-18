from django.conf.urls import url
from . import views
from .views import StudentCreateView, particularcallView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>[0-9]+)$', views.cususStudent, name='cusus_student'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^call/$', particularcallView.as_view()),
]