from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework import viewsets # type: ignore
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test APi View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditionald Django View',
            'Gives you the most control over you application logic',
            'is mapped manually to URLs',
        ]
    
        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello massage with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})
    

    def patch(self, request, pk=None):
        """Handle a patrial update of an object"""
        return Response({'method': 'PATCH'})
    

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""
        a_viewset= [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically map to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hellp!', 'a_viewset': a_viewset})
    

    def create(self, request):
        """Create new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """updating object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """updating parto of object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """remove object"""
        return Response({'http_method': 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """createing and updating profile"""
    serializer_class= serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
