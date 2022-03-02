from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from app.models import Tweet
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, TweetSerializer
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TweetsViewSet_day(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Last 24 Hours
    """
    date_from = datetime.datetime.now().date() - datetime.timedelta(days=1)
    now = datetime.datetime.now()
    queryset = Tweet.objects.filter(date__gte=date_from, date__lte=now)
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', ]


class TweetsViewSet_week(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Last 7 Days
    """
    date_from = datetime.datetime.now().date() - datetime.timedelta(days=7)
    now = datetime.datetime.now()
    queryset = Tweet.objects.filter(date__gte=date_from, date__lte=now)
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', ]


class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    # 1. List all
    def get(self, user_id):
        '''
        List all the todo items for given requested user
        '''
        tweet = Tweet.objects.filter(user=user_id)
        serializer = TweetSerializer(tweet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
