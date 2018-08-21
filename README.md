### Instalar python3 python3-pip python3-virtualenv ###

```console
user@nombre_maquina:/# sudo aptitude install python3 python3-pip python3-virtualenv
```

## Crear el entorno virtual ##

```console
user@nombre_maquina:$ virtualenv -p python3 envAgencia
```

## Activar y actualizar el entorno virtual ##

```console
user@nombre_maquina:$ cd envAgencia
user@nombre_maquina:$ source bin/activate
(envAgencia) user@nombre_maquina:envAgencia$ pip install -U virtualenv pip
```

## instalar requisitos ##

```console
(envAgencia) user@nombre_maquina:envAgencia$ pip install -r requirements.txt
```

## Clonar el repositorio git ##

```console
(envAgencia) user@nombre_maquina:$ git clone https://github.com/gvizquel/ProyectoAgencia.git
```

### Inciar servidor de desarrollo ###

```console
(envAgencia) user@nombre_maquina:$ ./manage.py runserver
```

Si todo lo has hecho al pie de la letra y yo no cometí algún error de omisión deberían ver algo como esto:

```console
System check identified no issues (0 silenced).
March 25, 2018 - 12:15:56
Django version 2.x, using settings 'proyectoPrueba.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
```

>Para ver nuestro proyecto en funcionamiento, con el navegador web de su preferencia, abra la url <http://127.0.0.1:8000/admin>
