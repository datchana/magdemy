from django.urls import path
from .views import bookView, registerView

urlpatterns = [
    path('api/book/', bookView.as_view(), name='book'),
    path('api/register/', registerView.as_view(), name='register'),
]