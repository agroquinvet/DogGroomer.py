# 🐶Doggroomer

Este repositorio contiene el código fuente de Doggroomer, una aplicación de gestión de turnos para peluquería canina y control de clientes. La aplicación está diseñada para ayudar a los propietarios de peluquerías caninas a organizar sus citas y mantener un registro de sus clientes y mascotas.

# ✨ Características

Gestión de Clientes: Registro y administración de los clientes y sus datos de contacto.
Gestión de Mascotas: Registro de mascotas con información detallada como raza y fecha de nacimiento.
Gestión de Turnos: Creación y administración de turnos para distintos servicios.
Autenticación y Autorización: Sistema de usuarios con permisos y autenticación personalizada.

# 🛠️ Tecnologías Utilizadas
Python 3.8+
Django 3.2+
SQLite: Base de datos utilizada en desarrollo.

# 📋 Requisitos
Python 3.8+
Django 3.2+
pip (Python package installer)


# ⚙️ Instalación
Sigue estos pasos para configurar el proyecto en tu máquina local:

Clona el repositorio:
git clone git@github.com:agroquinvet/DogGroomer.py.git
cd doggroomer

Crea un entorno virtual:
python -m venv env
source env/bin/activate  
En Windows usa `env\Scripts\activate`

Instala las dependencias:

python manage.py makemigrations
python manage.py migrate

Crea un superusuario:
python manage.py createsuperuser

python manage.py runserver
Accede a la aplicación:

Abre tu navegador y Ve a http://127.0.0.1:8000 para acceder a la aplicación.

# 🚀 Uso
ingresa al software con el super usuario creado desde python  
registra un cliente por su numero de documento y luego una o varias mascotas para este cliente  
una vez agendados toma un turno para la mascota de acuerdo al servicicio que quieras ofrecer   
y luego peudes ir a la agenda y mirar el turno agendando en el dia y horario asignado. 

# 🤝 Contribución
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Sube tus cambios (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

# 📄 Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.

# 📬 Contacto
Para cualquier duda o consulta, puedes contactarnos en maryangelin.quintero@gmail.com


