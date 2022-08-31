from django.urls import path
from .views import TaskListView, TaskDetailView, TaskDeleteView, TaskUpdateView, TaskCreateView, CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView
urlpatterns = [

    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),

    path('login', CustomLoginView.as_view(next_page='tasks'), name='login'),
    path('register', RegisterPage.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
]