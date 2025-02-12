from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test APi View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditionald Django View',
            'Gives you the most control over you application logic',
            'is mapped manually to URLs',
        ]
    
        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})