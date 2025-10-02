# Trabajo desarrollo web
<h3>El trabajo está realizado por: </h3>
<h4>🎮 Joaquin Leonel Orlando (?)<br>
🕹️ Martín Alberto Villafañe (114769)<br>
👾 Nicolás Ignacio Araujo (114312)<br></h4>

Con el tema dentro de la pagina web sentimos que el trabajo está bien realizado y bastante bien guiado.
No haria falta una guia más externa más que la misma informacion que muestra la pagina web. 

![HURRA](static/images/hurra.jpeg)

Esperemos que les guste el diseño de la pagina. <br>
Por mas de que las ideas pricipales salieron de un template ya creado, tuvimos q rediseñar todos los textos y ademas, sumarle pedidos del trabajo practico, siendo algo complicado el poder adaptar nuestras ideas dentro del marco ya creado del template.
# OJO
Dentro del "crearentorno.sh", (puede ser algo confuso en el final) entrando al menu del script: <br>
1. Primero pedira el nombre de la carpeta en donde te gustaria crear el entorno (las carpetas templates y static siempre tendrán el mismo nombre).<br>
Luego van a salir muchas palabras raras (es solo el flask instalando), saldra mucho texto pero el final es lo importante

![pero](static/images/ojito.jpeg)

2. Cuando el Script dice si desea correr el entorno virtual, la opción elegida para <strong>SI</strong> debe ser exactamente "1" (sin las comillas), caso contrario el entorno no será iniciado provocando que se cierre el Script y, aunque haya creado los directorios y los archivos Pipfile, no se iniciará el entorno para poder comenzar a trabajar.

![ojo](static/images/ojo.jpeg)

3. Si se desea correr el entorno virtual, la forma que más recomiendo (consejo del que escribe) es utilizando el comando:
```bash
source .venv/bin/activate
```
Esto activará el entorno de manera manual, otra forma posible es corriendo el Script nuevamente y colocando el mismo nombre de directorio elegir la opcion 1 para levantar el entorno (no recomendada ya que podría haber un error de tipeo y crear un nuevo entorno).

4. En caso de querer borrar el entorno por cualquier razón, se puede correr el Script con el parámetro optativo "-d"
```bash
bash crearentorno.sh -d
```
Y se deberá indicar qué carpeta/directorio se desea borrar (hacerlo a conciencia).

<h2>FIN DEL COMUNICADO</h2>

¡Esperamos que esto te ayude!



