# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import UserProfile
from .Serializer import UserSerializer

class UserListView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
    	queryset = UserProfile.objects.all()
    	username = self.request.query_params.get('username')
    	print username,type(username)
    	if username:
    		#username1=str(username)
    		# print username1
    		# print type(username1)
    		queryset = queryset.filter(username=str(username))
    		print queryset
    	return queryset