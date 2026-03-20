from django.urls import path
from apps.users import views

urlpatterns = [
    path("", views.CreateUserView.as_view()),
    path("<int:pk>/", views.UserDetailView.as_view())
]