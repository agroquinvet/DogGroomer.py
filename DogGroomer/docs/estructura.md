# Estructura del Proyecto Doggroomer

Este proyecto de Django gestiona turnos, clientes y usuarios para una peluquería canina. A continuación, se describe la estructura de carpetas y archivos principales, con las funciones de cada aplicación.

## Estructura de Archivos y Carpetas

```plaintext  
doggroomer/   
├── doggroomer/           # Aplicación principal del proyecto  
│   ├── __init__.py       # Indica que esta es una carpeta de Python  
│   ├── settings.py       # Configuración general (bases de datos, apps instaladas, etc.)  
│   ├── urls.py           # Rutas principales del proyecto  
│   ├── asgi.py           # Configuración para despliegue asíncrono  
│   └── wsgi.py           # Configuración para despliegue síncrono  
│  
├── account/              # Gestión de usuarios y autenticación  
│   ├── migrations/       # Archivos de migración de la base de datos para account  
│   ├── templates/        # Plantillas HTML para autenticación de usuarios  
│   ├── __init__.py         
│   ├── models.py         # Modelos de usuario personalizados  
│   ├── views.py          # Vistas para el manejo de usuarios (registro, login, perfil)  
│   └── urls.py           # Rutas específicas para account  
│  
├── acerca/               # Página home y contacto de la aplicación  
│   ├── templates/        # Plantillas HTML para home y contacto  
│   ├── __init__.py         
│   ├── views.py          # Vistas para la página de inicio y contacto  
│   └── urls.py           # Rutas para home y contacto  
│  
├── agenda_turnos/        # Manejo del calendario y turnos asignados  
│   ├── migrations/         
│   ├── templates/        # Plantillas para ver y gestionar turnos  
│   ├── __init__.py         
│   ├── models.py         # Modelos de turnos, incluyendo fechas, clientes y servicios  
│   ├── views.py          # Lógica para la gestión del calendario y asignación de turnos  
│   └── urls.py           # Rutas para calendario y administración de turnos  
│  
├── clientes/             # Registro de clientes y sus mascotas  
│   ├── migrations/         
│   ├── templates/        # Plantillas para gestionar clientes y mascotas  
│   ├── __init__.py         
│   ├── models.py         # Modelos de clientes y mascotas  
│   ├── views.py          # Vistas para administrar el registro de clientes y mascotas  
│   └── urls.py           # Rutas para el registro y gestión de clientes y mascotas  
│  
├── manage.py             # Herramienta de línea de comandos de Django  
├── requirements.txt      # Dependencias del proyecto  
└── README.md             # Documentación inicial del proyecto  
