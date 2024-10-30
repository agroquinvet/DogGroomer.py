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

Abre tu navegador y ve a http://127.0.0.1:8000 para acceder software.  
