# AppCoderPancho

Este proyecto es una aplicación web desarrollada con Django siguiendo el patrón MVT (Modelo - Vista - Template). Simula una plataforma estilo blog/inventario, permitiendo gestionar productos, categorías y perfiles de usuario, además de incluir funcionalidad de búsqueda.

## 🧩 Funcionalidades principales

- ✅ Herencia de plantillas HTML usando `base.html`.
- ✅ Modelo de al menos 3 clases (`Producto`, `CategoriaProducto`, `PerfilUsuario`).
- ✅ Formularios para crear datos en cada uno de los modelos.
- ✅ Formulario para buscar productos por nombre.
- ✅ Sistema de login de usuarios.
- ✅ Vista de configuración de perfil con personalización de color y foto.

---

## 📦 Modelos creados

1. **Producto**: nombre, descripción, precio, categoría, fecha de ingreso.
2. **CategoriaProducto**: nombre, descripción.
3. **PerfilUsuario**: usuario, nombre, apellido, email, foto de perfil, color de página, modo oscuro.

---

## 🧪 ¿Cómo probar el proyecto?

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/PanchoBarraza1/AppCoderPancho.git
   cd AppCoderPancho
   ```

2. **Crea y activa el entorno virtual**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # En Windows
   ```

3. **Instala dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Inicia el servidor**
   ```bash
   python manage.py runserver
   ```

6. **Accede a la app**
   - Ir a `http://127.0.0.1:8000/`

---

## 🚀 Funcionalidades clave

| Sección                        | Ruta                                | Descripción                                       |
|-------------------------------|-------------------------------------|--------------------------------------------------|
| Home                          | `/`                                 | Página principal con menú                        |
| Login                         | `/login/`                           | Iniciar sesión                                   |
| Crear producto                | `/producto/crear/`                  | Formulario para agregar nuevos productos         |
| Ver inventario                | `/inventario/`                      | Lista de productos con campo de búsqueda         |
| Crear categoría               | `/categoria/crear/`                 | Crear nueva categoría de productos               |
| Configuración de usuario      | `/configuracion/`                   | Cambiar nombre, color y foto de perfil           |

---

## 🧪 Usuario de prueba

Puedes crear tu propio usuario desde el login, o usar uno de prueba si se configuró alguno manualmente en la base.

---

## 📁 Estructura destacada

```
AppCoder/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── inventario_list.html
│   └── configuracion.html
├── static/
│   └── estilos.css
```

---

## 📌 Notas

- Este proyecto es parte de una entrega para el curso de Python con Django.
- El nombre del repositorio sigue la convención: `AppCoderPancho`.

---

## 🌐 Autor

Francisco Barraza – [GitHub](https://github.com/PanchoBarraza1)
