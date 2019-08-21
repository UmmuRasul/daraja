from django.contrib.auth.models import User
from mpesapp.api.serializers import LNMOnlineSerializer
from rest_framework.generics import CreateAPIView
from mpesapp.models import LNMOnline
from mpesapp.api.serializers import LNMOnlineSerializer
#from rest_framework.permissions import IsAdminUser

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    

    def create(self, request):
        print(request.data, 'This is request.data')