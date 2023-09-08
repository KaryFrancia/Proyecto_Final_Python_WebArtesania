# Proyecto Final Curso de Python - CoderHouse
#### Comisión: 43870
#### Alumna: Kary Francia Vásquez

- [Nombre del proyecto](#nombre_del_proyecto)
- [versión](#versión)
- [Requerimientos](#requerimientos)
- [Instalación](#instalación)
- [Descripción](#descripción)
- [Funcionalidades](#funcionalidades)
- [Pruebas](#pruebas)
- [Contribución](#contribución)
- [Video](#video)

## Nombre del Proyecto
Pericotitos Artesanos - Web Tipo blog para venta de artesanías.

## Versión
1.0

## Requerimientos
#### Tecnología Utilizada
##### Front-End
- HTML 5
- CSS 3
- Bootstrap 5
- Javascript
##### Back-End
- Python 3.11.4
- Django 4.2.3

## Instalación

1. Clona este repositorio en tu máquina local: git clone https://github.com/KaryFrancia/Proyecto_Final_Python_WebArtesania.git
2. Navega hacia el directorio del proyecto: cd artesanía
3. Crea y activa un entorno virtual:
- Windows:
  ```
  python -m venv myenv
  myenv\Scripts\activate
  ```
- macOS/Linux:
  ```
  python3 -m venv myenv
  source myenv/bin/activate
  ```
4. Ejecuta el servidor de desarrollo Django:  `python manage.py runserver`
5. Accede a la aplicación en tu navegador visitando: `http://127.0.0.1:8000/`

## Descripción 
##### Pericotitos Artesanos Marketplace

Pericotitos Artesanos Marketplace, es una plataforma en línea dedicada a la promoción y venta de artesanías únicas y hechas a mano. La web está diseñada exclusivamente para los miembros de la comunidad de Pericotitos Artesanos, esta plataforma ofrece a los usuarios una experiencia interactiva para compartir y vender sus creaciones artesanales y conectarse en un entorno amigable.

## Funcionalidades
##### Inicio de Sesión y Registro:
Para acceder a todas las funciones de la plataforma (excepto "Ver tutotrial en video", "buscar" y "Acerca de mí") los usuarios deben iniciar sesión con sus credenciales existentes o registrarse si aún no tienen una cuenta. Una vez que la autenticación es exitosa, los usuarios son redirigidos al inicio de la página web.

##### Perfil de Usuario:
Cada usuario tiene un perfil personalizable donde pueden mostrar su información agregando una foto de perfil, su avatar, sus datos personales. También pueden editar estos datos o cambiar su contraseña y tiene la opción de eliminar su perfil, pero en ese caso no podrá administrar sus mensajes con otros usuarios, ya que la administración de mensajería se encuentra ubicada en la página de perfil.

##### Cambiar Contraseña:
Los usuarios pueden cambiar su contraseña en cualquier momento desde la sección de editar perfil.

##### Mensajería:
Dentro de la página de perfil de usuario, los miembros pueden acceder a su bandeja de entrada de mensajes. Pueden ver los mensajes recibidos y enviar nuevos mensajes a otros usuarios, lo que facilita la comunicación y las transacciones.

##### Categorías de Productos:
Los usuarios pueden explorar una amplia gama de categorías de productos artesanales, que incluyen:
Mates
Vidrios
Joyas
Pinturas
Especiales

##### Publicación de Productos:
Desde la página de inicio, en la sección agregar artesanías, los miembros de Pericotitos Artesanos pueden crear y publicar sus productos artesanales en la plataforma. Pueden cargar imágenes, descripciones detalladas y establecer precios para sus creaciones.

##### Visualización y Comentarios:
Los usuarios pueden explorar las diversas categorías y productos artesanales en la plataforma. Además, tienen la opción de comentar y dejar reseñas en los productos que deseen, lo que fomenta la interacción y la retroalimentación entre los miembros de la comunidad.

##### Privilegios de Edición y Eliminación:
Los autores de las publicaciones tienen la capacidad de editar y eliminar sus propios productos artesanales, lo que les brinda un control total sobre sus listados. No pueden editar ni eliminar productos agregados por otros usuarios, pero si pueden ver el detalle de los mismos. 

##### Búsqueda de Productos:
Incluso estando fuera de la sesión, los visitantes pueden acceder a la funcionalidad de búsqueda de productos utilizando palabras clave. Esto permite a los usuarios, si es que así lo desean, buscar artesanías específicas sin necesidad de iniciar sesión. Tanto la búsqueda con sesión iniciada como fuera de sesión solo permite mostrar el detalle del producto.

##### Tutorial en Video:
Fuera del inicio de sesión, también se encuentra el botón Ver tutorial en video, este tutorial muestra cómo utilizar la plataforma de manera efectiva para vender artesanías hechas a mano.

##### Cerrar Sesión y Volver a Iniciar Sesión:
Los usuarios pueden cerrar sesión de forma segura cuando lo deseen y, si lo desean, pueden volver a iniciar sesión en cualquier momento.

##### Acerca de Mí:
La plataforma incluye una sección "Acerca de Mí" donde se comparte información acerca de la creadora de la página web y el proyecto Pericotitos Artesanos.

## Pruebas

Para ver los casos de pruebas realizados, accede al archivo titulado "casos_de_prueba_proyecto_final_python.xlsx" el cual se encuentra en el presente repositorio https://github.com/KaryFrancia/Proyecto_Final_Python_WebArtesania/blob/master/casos_de_prueba_proyecto_final_python.pdf

## Contribución: 
Si deseas contribuir con este proyecto, sigue estos pasos:

1. Fork the repository.
2. Create a branch for your changes: `git checkout -b feature/new-feature`
3. Make your changes and commit them: `git commit -m "Add new feature"`
4. Push your changes to your fork: `git push origin feature/new-feature`
5. Open a pull request on GitHub.

## Video
Se crea este video para una visión completa de cómo utilizar la plataforma y aprovechar al máximo todas las opciones disponibles. ¡Espero que encuentres esta guía útil y que disfrutes de tu experiencia en Pericotitos Artesanos Marketplace!
Para acceder al video, simplemente haz clic en el siguiente enlace: https://www.youtube.com/watch?v=UL9SGg-N5nk





