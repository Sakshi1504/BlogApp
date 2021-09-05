from Home.models import Profile
from Home.helpers import generatestring
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

class LoginView(APIView):

    def post(self, request):
        response={}
        response['status']=500
        response['message']="Something went wrong."
        try:
            data=request.data

            if data.get('username') is None:
                response['message']="key/parameter username not found"
                raise Exception("key username not found.")

            if data.get('password') is None:
                response['message']="key/parameter password not found"
                raise Exception("key password not found.")

            checkuser=User.objects.filter(username = data.get('username')).first()

            if checkuser is None:
                response['message']="Invalid Username, Not Found."
                raise Exception("Invalid Username, Not Found.")

            validuser=authenticate(username=data.get('username'), password=data.get('password'))

            if validuser is None:
                response['message']="Invalid Credentials(Password)"
                raise Exception("Invalid Credentials(Password)")
            else:
                login(request, validuser)
                response['message']="Badhai ho, aapko login hua hai!! XD "
                response['status']=200


        except Exception as e:
            print(e)

        return Response(response)


LoginViewobj = LoginView.as_view()


class RegisterView(APIView):

    def post(self, request):
        response={}
        response['status']=500
        response['message']="Something went wrong."
        try:
            data=request.data

            if data.get('username') is None:
                response['message']="key/parameter username not found"
                raise Exception("key username not found.")

            if data.get('password') is None:
                response['message']="key/parameter password not found"
                raise Exception("key password not found.")
            
            if data.get('email') is None:
                response['message']="key/parameter email not found"
                raise Exception("key email not found.")

            checkuser=User.objects.filter(username = data.get('username')).first()

            if checkuser:
                response['message']="User Already Taken. Try with some other username."
                raise Exception("User Already Taken. Try with some other username.")

            userobj=User.objects.create(email=data.get('email'), username=data.get('username'))
            userobj.set_password(data.get('password'))
            userobj.save()
            token=generatestring(10)

            Profile.objects.create(user=userobj, token=token)
            response['message']="You are successfully registered. Please login to Continue."
            response['status']=200


        except Exception as e:
            print(e)

        return Response(response)


RegisterViewobj = RegisterView.as_view()