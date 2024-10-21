from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail
from django.conf import settings


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ContactMessageView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_contact_email(request.data['email'], request.data['message'])
            return Response({'code': 200, 'message': 'Message sent successfully!'}, status=status.HTTP_200_OK)
        return Response({'code': 400, 'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


def send_contact_email(user_email, user_name, message):
    # Email to the admin or service provider
    send_mail(
        subject="New Contact Form Submission",
        message=f"""Hello Eby,
        You received a new message from {user_name}
        Message : {message}
        Email : {user_email}""",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['cybe1990@gmail.com'],
    )

    # Email to the user
    send_mail(
        subject="Thank you for your message",
        message=f"""Hello {user_name},

        We received your message and will get back to you soon!

        Thank you.

        Best Regards,
        Eby Chacko
        Mob: +35389 233 6291
        """,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
    )