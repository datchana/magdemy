from django.shortcuts import render
from .serializers import bookFormSerializer, registerFormSerializer
from rest_framework import status
from root.response import GenericResponse
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class bookView(GenericAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = bookFormSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return GenericResponse(success_msg="Your form is submitted successfully",
                                   status=status.HTTP_201_CREATED
                                   )
        else:
            return GenericResponse(error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class registerView(GenericAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = registerFormSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return GenericResponse(success_msg="Your form is submitted successfully",
                                   status=status.HTTP_201_CREATED
                                   )
        else:
            return GenericResponse(error_msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



