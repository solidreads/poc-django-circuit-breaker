
from django.conf import settings

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

import requests
from pybreaker import CircuitBreaker, CircuitBreakerError


circuit_breaker = CircuitBreaker(
    settings.CIRCUIT_BREAKER_SETTINGS['DEFAULT']['fail_max'], 
    settings.CIRCUIT_BREAKER_SETTINGS['DEFAULT']['reset_timeout']
)

@circuit_breaker
def make_get_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error en la respuesta del servidor")
    return response.json()

class MicroserviceView(views.APIView):

    def get(self, request):
        try:
            data = make_get_request('http://microservicio-pedido:8001/pedidos')
            return Response(data, status=status.HTTP_200_OK)
        except CircuitBreakerError:
            return Response({"error": "El servicio externo está actualmente inaccesible"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
