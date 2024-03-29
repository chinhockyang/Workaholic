from django.contrib import admin, auth
from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:pk>/', views.projectPage, name="projectPage"),
    path('<str:pk>/leave_project/', views.leaveProject, name="leaveProject"),

    path('<str:pk>/delete_member/<str:member_pk>/', views.deleteMember, name="deleteMember"),
    path('<str:pk>/set_admin/<str:member_pk>/', views.setAdmin, name="setAdmin"),
    path('<str:pk>/remove_admin/<str:member_pk>/', views.removeAdmin, name="removeAdmin"),

    path('<str:pk>/todo/', include('todo.urls')),
    path('<str:pk>/board/', include('board.urls')),
    path('<str:pk>/calendar/', include('cal.urls')),
    path('<str:pk>/forum/', include('forum.urls')),
    path('<str:pk>/delete_project/', views.deleteProject, name="deleteProject")
]
