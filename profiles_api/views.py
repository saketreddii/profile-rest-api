from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns list API features"""
        an_apiview =[
        'Users HTTP methods functions (get,post,patch,put,delete)',
        'Is similar to an traditional Django view',
        'Gives you most of the control over the application logic',
        'Is mapped manually to URL s',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
