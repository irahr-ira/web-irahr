# Directiva: Ejecutar Servidor Local

## Objetivo
Ejecutar un servidor HTTP local para servir los archivos estáticos de la landing page y permitir el funcionamiento correcto de formularios (FormSubmit) y otros recursos que requieren protocolo HTTP/HTTPS en lugar de `file://`.

## Entradas
- Puerto: 8000 (por defecto) o el siguiente disponible.
- Directorio Raíz: Directorio actual del proyecto.

## Pasos
1. Verificar si el puerto 8000 está libre.
2. Iniciar `http.server` de Python en el puerto 8000.
3. Imprimir la URL de acceso: `http://localhost:8000`.

## Restricciones y Advertencias
- **FormSubmit:** Requiere que la página sea servida por un servidor web para validar el `Referer`.
- **Bloqueo:** El servidor bloqueará la terminal. En contexto de agente, ejecutar en segundo plano o gestionar la sesión.
