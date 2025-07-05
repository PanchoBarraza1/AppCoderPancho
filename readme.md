# TuPrimeraPaginaBarraza

Este proyecto es una aplicación web desarrollada con Django siguiendo el patrón MVT (Modelo - Vista - Template). Simula una plataforma estilo blog/inventario, permitiendo gestionar productos, categorías y perfiles de usuario, con funcionalidades como búsqueda, personalización de la experiencia, y gestión de sesión.

## 🧩 Funcionalidades principales

- ✅ Home con mensaje de bienvenida personalizado.
- ✅ Herencia de plantillas HTML usando `base.html`.
- ✅ Modelo de al menos 3 clases (`Producto`, `Categoria`, `PerfilUsuario`).
- ✅ Formularios para crear y editar cada modelo.
- ✅ CRUD completo de productos.
- ✅ Formulario de búsqueda por nombre de producto.
- ✅ Configuración de usuario con foto de perfil, colores y modo oscuro.
- ✅ Validación de categorías duplicadas.
- ✅ Mensajes de éxito para crear, editar, eliminar o cerrar sesión.
- ✅ Login, registro y logout seguro con POST.

---

## 📦 Modelos creados

1. **Producto**: nombre, descripción, precio, cantidad, categoría, usuario.
2. **Categoria**: nombre (único).
3. **PerfilUsuario**: usuario, nombre, apellido, email, color, modo oscuro, foto de perfil.

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
   - Home: `http://127.0.0.1:8000/`
   - Inventario: `http://127.0.0.1:8000/inventario/`

---

## 🚀 Funcionalidades clave

| Sección                        | Ruta                                | Descripción                                     |
|-------------------------------|-------------------------------------|--------------------------------------------------|
| Home                          | `/`                                 | Página de bienvenida                             |
| Login                         | `/login/`                           | Iniciar sesión                                   |
| Logout                        | `/logout/`                          | Cerrar sesión (requiere POST)                    |
| Registro                      | `/registro/`                        | Crear nuevo usuario                              |
| Inventario                    | `/inventario/`                      | Lista de productos del usuario                   |
| Crear producto                | `/producto/crear/`                  | Formulario para agregar productos                |
| Editar producto               | `/editar/<id>/`                     | Modificar un producto existente                  |
| Eliminar producto             | `/eliminar/<id>/`                   | Eliminar un producto                             |
| Crear categoría               | `/categoria/crear/`                 | Crear nuevas categorías                          |
| Configuración de usuario      | `/configuracion/`                   | Personalizar colores, foto y preferencias        |
| Blog                          | `/pages/`                           | Lista de páginas (posts) públicas                |
| Ver detalle del post          | `/pages/<id>/`                      | Ver contenido completo del post                  |
| Crear nuevo post              | `/pages/crear/`                     | Solo para usuarios logueados                     |
| Editar/Borrar post            | `/pages/<id>/editar/`               | Solo el autor puede hacerlo                      |
| Acerca de mí                  | `/about/`                           | Página personal visible desde navbar             |
| Bandeja de entrada            | `/mensajes/bandeja/`                | Ver mensajes recibidos                           |
| Leer mensaje                  | `/mensajes/mensaje/<id>/`           | Marcar como leído al entrar                      |
| Enviar mensaje                | `/mensajes/enviar/`                 | Buscar usuario, completar asunto y contenido     |

---

## 🛠 Herramientas utilizadas

- Django 5.x
- Python 3.13
- SQLite
- CKEditor (para texto enriquecido en posts)
- Bootstrap 5 (CDN)

## 🧪 Usuario de prueba

Puedes registrarte con tu propio usuario desde `/registro/`.

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
│   ├── producto_form.html
│   ├── categoria_form.html
├── static/
│   └── estilos.css
ProyectoCoder/
├── settings.py
├── urls.py
```

---

## 📌 Notas

- Este proyecto es parte de una entrega para el curso de Python con Django.
- El nombre del repositorio sigue la convención: `TuPrimeraPaginaBarraza`.

---

## 🌐 Autor

Francisco Barraza – [GitHub](https://github.com/PanchoBarraza1)
