Blog Musical
-----------------------------------------------------------------------------------------------------------------
Desarrollado por Magali Kerszenblat y William Dodera

Creamos el proyecto en conjunto utilizando github y anydesk para ir editando el trabajo.
-----------------------------------------------------------------------------------------------------------------
Descripción del Proyecto:

Este proyecto trata del desarrollo de un blog mediante el Framework Django donde el usuario puede compartir sus
creaciones musicales o sus opiniones respecto a alguna canción o genero musical mediante un post. Mediante la mensajería
los usuarios pueden interactuar entre si y contactarse.
 
Los usuarios pueden colocarse un avatar en su perfil y pueden modificarlo al igual que el nombre de usuario que utilicen. 
Si el usuario no está registrado deberá hacer click en "Crear usuario".

El usuario administrador podra modificar los post y los usuarios de todos los usuarios; en cambio los usuarios convencionales
solo podran editar su propia información y posteos.
-----------------------------------------------------------------------------------------------------------------
Readme:

*Abrir la carpeta del proyecto desde visual studio code

*Abrir la terminal

*Instalar:
		Python        3.10.5
		pip           22.1.2
		virtualenv    20.14.1

*Activar el entorno virtual: dir> myvenv/Scripts/activate

*Instalar los requerimientos: dir> pip install -r requirements.txt

Una vez que todo este instalado correctamente:

*Moverse al directorio del proyecto: dir> cd blog_musical

*Para ejecutar se debe correr el comando: dir> python manage.py runserver

*Abrir el navegador y colocar en la url la ip del local host.

*Lo primero que se va a observar es la pantalla de inicio (Home).

*Hacer click en el botón que dice "Crear usuario":
  -Rellenar los campos para registrar el nuevo usuario.

*Una vez que el usuario esta logeado puede editar su perfil de usuario y su avatar. 
*Además el usuario puede crear y eliminar posts desde "Mis posts".
*Desde la vista de Blog se puede observar los posts creados por nosotros y también los de los demás usuarios.
*Desde "Mensajes" el usuario puede enviar y recibir mensajes de otros usuarios.
