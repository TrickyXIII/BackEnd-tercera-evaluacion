# Proyecto Evaluación 3 - Tienda Django


## Funcionalidades
* Catálogo de productos con categorías y buscador.
* Filtro para ordenar productos por precio (menor/mayor).
* Formulario para hacer pedidos y subir imágenes de referencia.
* Sistema de seguimiento usando un código único.
* Panel de administración para gestionar insumos, productos y pedidos.

# Cómo instalar y ejecutar

## 1. Clona este repositorio:

Bash
git clone https://github.com/TrickyXIII/BackEnd-tercera-evaluacion

## 2. Entrar a la carpeta:

[Bash]
cd BackEnd-tercera-evaluacion

## 3. Crea y activa tu entorno virtual:

python -m venv venv

### Si usas Git Bash
source venv/Scripts/activate

### Si usas Windows:
venv\Scripts\activate

### Si usas Mac/Linux:
source venv/bin/activate

## 4. Instalar lo necesario:

pip install -r requirements.txt

## 5. Preparar la base de datos:

python manage.py migrate

## 6. Enciende el servidor:

python manage.py runserver


# Datos de acceso:

Página principal: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Usuario: admin

Clave: admin
