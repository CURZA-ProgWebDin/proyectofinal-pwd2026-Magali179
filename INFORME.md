ESTE PROYECTO NO PUDO SER VERIFICADO, NI LA PARTE DEL FRONTEND NI LA DEL BACKEND DEBIDO A QUE 
MI PC SE DAÑO, SOLO PUDE ASEGURARME DE REALIZAR LA ENTREGA ANTES DE PERDER ARCHIVOS.

1. Justificación de la decisión de la Parte 1

Se eligió la Opción B, utilizando un service por dominio (AuthService, ProductosService, CategoriasService, ProveedoresService y MovimientosService).

Esta organización permite separar las llamadas a la API, haciendo que el código sea más ordenado, fácil de mantener y reutilizable. Los stores solo manejan el estado de la aplicación, mientras que los services se encargan de la comunicación con el backend.

2. ¿Cómo decidieron almacenar y verificar el rol del usuario en el frontend? ¿Qué pasa si alguien edita manualmente el localStorage para cambiar su rol?

El token, el nombre, el rol y el estado de autenticación se almacenan en un store de Pinia con persistencia en localStorage.

El frontend utiliza el rol para mostrar u ocultar opciones de la interfaz y para controlar el acceso mediante los guards de Vue Router. Sin embargo, el frontend no es la fuente de seguridad. Si un usuario modifica manualmente el localStorage, el backend continúa verificando el token y el rol mediante JWT antes de permitir el acceso a los endpoints protegidos. Por lo tanto, modificar el almacenamiento local no otorga permisos reales.

3. ¿Por qué la validación de stock insuficiente existe tanto en el frontend como en el backend? ¿Cuál es la fuente de verdad?

La validación en el frontend mejora la experiencia del usuario, ya que permite mostrar una advertencia antes de enviar la solicitud.

La validación del backend es la realmente importante, porque garantiza la integridad de los datos aunque la petición provenga de otro cliente o aunque alguien modifique el frontend.

4. ¿Qué problemas de CORS pueden surgir al consumir esta API desde Vite y cómo se resuelven en este proyecto?

Al ejecutarse el frontend y el backend en distintos puertos, el navegador puede bloquear las solicitudes por la política de CORS.

En este proyecto el problema se resuelve configurando un proxy en vite.config.js, de manera que el frontend realiza las peticiones al mismo origen durante el desarrollo y Vite las redirige al backend.