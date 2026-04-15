# python_coderhouse_final_project
trabajo final de django para el curso de coderhouse
# IT Office Inventory – Django Project

## 📌 Descripción

Aplicación web desarrollada con Django para la gestión de inventario de insumos y herramientas de IT dentro de una oficina.

Permite registrar, visualizar, editar y eliminar distintos elementos como cables, memorias RAM, discos, herramientas, entre otros. También incluye autenticación de usuarios y perfiles.

---

## 🚀 Funcionalidades principales

* Sistema de autenticación:

  * Registro de usuarios (Signup)
  * Inicio de sesión (Login)
  * Cierre de sesión (Logout)

* Perfil de usuario:

  * Visualización de datos personales
  * Edición de perfil

* Gestión de inventario (CRUD completo):

  * Crear insumos
  * Listar insumos
  * Ver detalle
  * Editar
  * Eliminar

* Workstations:

  * Listado
  * Detalle

* Navegación:

  * Home
  * About
  * Navbar presente en todas las vistas

* Panel de administración (Django Admin) para todos los modelos

* Restricción de acceso:

  * Solo usuarios autenticados pueden crear, editar o eliminar registros

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/405141-Ziade-Alejandro/python_coderhouse_final_project.git
cd python_coderhouse_final_project
```

2. Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. Aplicar migraciones:

```bash
python manage.py migrate
```

4. Cargar datos iniciales necesarios:

```bash
python manage.py loaddata inventory/fixtures/supplies_types.json
python manage.py loaddata inventory/fixtures/states.json
```

5. Ejecutar el servidor:

```bash
python manage.py runserver
```

---

## 📂 Estructura del proyecto

* `inventory/` → App principal (insumos, estados, tipos)
* `accounts/` → Autenticación y perfiles de usuario
* `core/` → Vistas generales (home, about, base template)

---

## 🎥 Video demostración

Link al video (Loom):

```
https://www.loom.com/share/17ca1039781a4bfa8cf2aea0ed9fc504
```

---

## 🧪 Requisitos cumplidos

* Aplicación en Django
* CRUD completo de modelo principal
* Uso de Class Based Views
* Uso de mixins (LoginRequiredMixin)
* Uso de decoradores
* Sistema de autenticación completo
* Perfil de usuario editable
* Template base con herencia
* Navbar funcional
* Vista Home y About
* Admin configurado
* Archivo `.gitignore` configurado correctamente
* `requirements.txt` incluido
* Base de datos excluida del repositorio

---

## 🔮 Futuras mejoras

* Mejorar la interfaz de usuario (UI/UX)
* Agregar comentarios al código para facilitar mantenimiento futuro
* Implementar CRUD para modelos auxiliares (States, SupplyTypes)
* Agregar búsqueda y filtros avanzados
* Implementar paginación en listas
* Subida de imágenes para insumos
* Sistema de logs o historial de cambios
* Tests automáticos

---

Proyecto desarrollado como entrega final del curso de Django.
