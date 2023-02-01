POC de Circuit Breaker usando django

En la prueba se contiene 2 microservicios (micro servicio usuario y microservicio pedido)

micorservicio usuario que hara una petición al microservicio pedido mediante un get
y de acuerdo ala configuracion en la vista  microservicio-usuario/app/usuario/views.py se crea un objeto de tipo CircuitBreaker con fail_max establecido en 5 y reset_timeout en 30 segundos. Esto significa que si la función decorada falla 5 veces en un período de 30 segundos, el circuit breaker se activará

instalación

```shell
docker-compose up
```

mantente esuchando el log del servicio pedido
```shell
docker logs -f --tail 10 id_contenedor_pedidos
```

realiza 5 peticiones curl al microservicio de usuarios que a su vez consultara el servicio de pedidos y observa como despues de 5 consultas a la sexta deja de realizar llamadas al servicio de pedidos
```shell
curl http://0.0.0.0:8000/usuarios/
```
