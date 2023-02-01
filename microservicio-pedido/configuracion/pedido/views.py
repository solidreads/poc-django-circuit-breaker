import time
from django.conf import settings
from rest_framework import views
from rest_framework.response import Response


# Create your views here.
class PedidoView(views.APIView):

    def get(self, request):
        
        return Response(status=500)
        # return Response({"detail": "La respuesta fue exitosa desde el servicio de pedido"})
