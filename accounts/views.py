from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username=username, password=password)
        serializer = UserSerializer(user)
        status = 201
        return Response(serializer.data, status=status)


class LoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        # 유저가 존재하는지 검사
        try:
            User.objects.get(username=username)

        # 유저가 존재하지 않을 경우
        except User.DoesNotExist:
            status = 400
            message = '존재하지 않는 아이디입니다.'
            return Response({'message': message}, status=status)

        # 유저가 존재할 경우
        else:
            user = authenticate(username=username, password=password)

            # 비밀번호가 잘못된 경우
            if user is None:
                status = 400
                message = '잘못된 비밀번호입니다.'
                return Response({'message': message}, status=status)

            # 로그인에 성공했을 경우
            else:
                jwt = self.create_jwt(user)
                status = 200
                message = '로그인에 성공하였습니다.'
                return Response(
                    {'message': message, 'jwt': jwt},
                    status=status
                )


    def create_jwt(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class LogoutView(APIView):

    def get(self, request):
        logout(request.user)
