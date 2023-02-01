POC de Circuit Breaker usando django

En la prueba se contiene 2 microservicios

micorservicio usuario que hara una petición al servicio pedido mediante un get
y de acuerdo ala configuracion en la vista  microservicio-usuario/app/usuario/views.py se crea un objeto de tipo CircuitBreaker con fail_max establecido en 5 y reset_timeout en 30 segundos. Esto significa que si la función decorada falla 5 veces en un período de 30 segundos, el circuit breaker se activará

instalación

```shell
docker-compose up
```
