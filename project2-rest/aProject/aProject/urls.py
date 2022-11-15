from django.contrib import admin
from django.urls import path, include
from myAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', views.TaskList.as_view()),
]