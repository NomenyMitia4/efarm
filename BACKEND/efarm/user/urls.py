from django.urls import path
from .views import UserView, LoginView

urlpatterns = [
    path('user/', UserView.as_view(), name='UserView'),
    path('user/<int:pk>/', UserView.as_view(), name='UserDelete'),  
    path('user/login/', LoginView.as_view(), name='LoginView')
]
