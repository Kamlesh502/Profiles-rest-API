from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloAPIView(APIView):
    """Test API View"""

    def get(self,resquest,format=None):
        """Return the list of APIView Featurees"""
        an_apiview=[
            'uses HTTP method',
            'django',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
