# Autentication-System
Objetivo:
Construir un vertical prototype (VP) simple de un mini‑portal con autenticación y un módulo de solicitudes. 
El objetivo es evaluar capacidades prácticas de desarrollo full stack.

Tiempo máximo de entrega: 48 horas.

## REQUERIMIENTO FUNCIONAL

1. Login
- Email + password
- Password hasheado
- Sesión con JWT o cookies (a elección del desarrollador)

2. Roles de usuario
El sistema debe contemplar tres tipos de usuario:

- Admin
- Empleado
- Cliente

3. Módulo de Solicitudes

Entidad: Solicitud

### Campos mínimos:
- id
- titulo
- descripcion
- estatus (open / closed)
- createdAt
- ownerId
- accountId

### Acciones por rol

Cliente
- Puede crear solicitudes
- Solo puede ver las solicitudes de su cuenta

Empleado
- Puede ver todas las solicitudes
- Puede cambiar el estatus de una solicitud

Admin
- Puede ver todas las solicitudes
- Puede cambiar el estatus
- Puede eliminar solicitudes

## INTERFAZ MÍNIMA

Debe existir al menos:

- Pantalla Login
- Pantalla Lista de Solicitudes (tabla simple)
- Opción para crear solicitud
- Botón para cerrar solicitud (solo empleado/admin)

No se evalúa diseño visual, sino funcionalidad.

## SEGURIDAD MÍNIMA

El sistema no debe permitir que un cliente vea solicitudes de otros clientes manipulando IDs.

Debe existir validación básica de inputs.

## STACK

El desarrollador puede utilizar cualquier lenguaje, framework o herramienta que prefiera.

Se espera:
- Backend API
- Base de datos
- Frontend mínimo funcional

## DATOS DE PRUEBA

Incluir usuarios seed:

- 1 Admin
- 1 Empleado
- 2 Clientes (de cuentas distintas)

Cada cuenta debe tener al menos 2 solicitudes de ejemplo.

## ENTREGABLES

Solo se requiere:

1. Repositorio del proyecto
2. Video corto (3–5 minutos) mostrando el funcionamiento de la plataforma

## EVALUACIÓN

Se evaluará principalmente:

- Claridad del código
- Arquitectura del proyecto
- Control de accesos correcto
- Modelado básico de datos
- Funcionamiento general
