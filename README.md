🐶 Doggroomer
Este repositorio contiene el código fuente de Doggroomer, una aplicación de gestión de turnos para peluquería canina y control de clientes. La aplicación está diseñada para ayudar a los propietarios de peluquerías caninas a organizar sus citas y mantener un registro de sus clientes y mascotas.

✨ Características
Gestión de Clientes: Registro y administración de los clientes y sus datos de contacto.
Gestión de Mascotas: Registro de mascotas con información detallada como raza y fecha de nacimiento.
Gestión de Turnos: Creación y administración de turnos para distintos servicios.
Autenticación y Autorización: Sistema de usuarios con permisos y autenticación personalizada.

🛠️ Tecnologías Utilizadas
Python 3.8+
Django 3.2+
SQLite: Base de datos utilizada en desarrollo.

📋 Requisitos
Python 3.8+
Django 3.2+
pip (Python package installer)


⚙️ Instalación
Sigue estos pasos para configurar el proyecto en tu máquina local:

Clona el repositorio:
git clone git@github.com:agroquinvet/DogGroomer.py.git
cd doggroomer

Crea un entorno virtual:
python -m venv env
source env/bin/activate  
# En Windows usa `env\Scripts\activate`

Instala las dependencias:

python manage.py makemigrations
python manage.py migrate

Crea un superusuario:
python manage.py createsuperuser

Ejecuta el servidor de desarrollo:
python manage.py runserver
Accede a la aplicación:

Abre tu navegador y ve a http://127.0.0.1:8000/admin para acceder al panel de administración.
Ve a http://127.0.0.1:8000 para acceder a la aplicación.

🚀 Uso
Acceso al Administrador de Django
Inicia sesión en el administrador de Django usando las credenciales del superusuario que creaste.
Desde el panel de administración, puedes gestionar clientes, mascotas, servicios y turnos.
Utiliza las funcionalidades de búsqueda, filtrado y ordenamiento para encontrar y organizar la información fácilmente.
Personalización y Desarrollo
Para añadir nuevas características, puedes modificar los archivos del proyecto y crear nuevas migraciones usando python manage.py makemigrations y python manage.py migrate.
Los archivos de configuración principal se encuentran en settings.py.
Los modelos se encuentran en models.py, y las vistas y URLs están en views.py y urls.py respectivamente.

🤝 Contribución
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Sube tus cambios (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

📄 Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.

📬 Contacto
Para cualquier duda o consulta, puedes contactarnos en maryangelin.quintero@gmail.com


