from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('classe/<str:classe>/', views.students_by_class, name='by_class'),
    path('<int:id>/', views.student_detail, name='detail'),
]