# Instalación

Lo primero de todo es tener una versión de Python instalada en nuestra máquina. Puedes encontrar una aquí https://www.python.org/downloads/<br>
En una terminal, nos situamos en la carpeta del proyecto en el que vamos a trabajar. Seguidamente, introducimos los siguientes comandos:<br>
`pip install fastapi`<br>
`pip install uvicorn`<br>
Estos instalarán las librerías que se han utilizado para la API REST del proyecto.

# Ejecución

Para ello, lo primero que tenemos que hacer es lanzar la API REST. Para hacer esto, en una terminal nos situamos en la carpeta del proyecto y escribimos los comandos:<br>
`cd src/API_REST`<br>
`uvicorn ApiRest:app --reload`<br>
Ya tenemos la API REST en funcionamiento y lista para ser llamada.

Lo siguiente que debemos hacer es: Abrir un nuevo terminal desde donde lanzar el comando que ejecutará la app. Como antes, nos situamos en la carpeta del proyecto en la terminal y escribimos el siguiente comando para situarnos en la carpeta donde está el "script" para lanzar la app.<br>
`cd src/Logica`<br>
Una vez situados en la carpeta del script, paso a explicar el funcionamiento de este sencillo comando:<br>
`python Main.py [argumentos]`<br>
Donde está la parte de argumentos escribimos el report, de los 3 que pedía la prueba, que queremos lanzar (report1, report2 o report3). Por ejemplo:<br>
-`python Main.py report2` Para generar el CSV del report 2 de la prueba.<br>
-`python Main.py report1 report2 report3` Para generar los 3 CSVs de la prueba. (El orden de los argumentos no importa)<br>
Y con esto generaría los CSVs nombrados en la carpeta Data del proyecto que uso para almacenar todos los CSVs. Obviamente en un caso real, el CSV se guardaría en otra carpeta de la máquina que tu le indicases o directamente mapearíamos el CSV a una BD.

# Sobre mi experiencia haciendo la prueba

Primero voy a contar el porqué elegí Python. La verdad es que me daba igual hacerlo en Python o JS (que eran las opciones que se recomendaban junto a php) ya que he programado en los dos lenguajes haciendo proyectos en la carrera (NodeJS para una asignatura, TypeScript + Angular para un proyecto y Python + PyQt para otro). Añadir que se más lenguajes como Java, C#, C, etc... Una vez llegados a este punto, quería que la prueba me sirviese para aprender. Leído el enunciado entendí que iba a trabajar con archivos CSV, algo que ya había hecho con JS y más o menos ya sé como funciona y quería aprender como Python trataba los CSV. Así que me decidí simplemente por eso.

Las dificultades que he encontrado son todas relacionadas a como trata Python los CSV. Por ejemplo el como poder extraer solo producto de la columna productos de orders.csv. Al final, entre el poco tiempo que he tenido por trabajos de la universidad y exámenes no he podido dedicarle el tiempo que me hubiese gustado para mejorar, quizás, la eficiencia con la que lo he hecho y haceros una interfaz con PyQt o Tkinter. Decir también que con una BD a la que poder mapear ciertos datos de los CSV hubiese sido infinitamente más facil porque no tendría que pensar en crear tablas en Python para luego juntarlas y transformarlas en el CSV final, sino que lo mapeo y de la BD extraigo la información ya estructurada.

El porqué de mi código lo comento en el mismo (aunque la guía del buen programador indica que no hay que hacer comentarios en el código, yo los hago para que sea más rápido de entender).

# Bibliografía que he usado para documentarme

-Para tratar argumentos de entrada por comandos:<br>
 https://www.youtube.com/watch?v=4ZcX5Prfix0&ab_channel=kipunaec<br>
-Para tratar los CSV como tablas:<br>
 https://stackoverflow.com/questions/62480335/querying-csv-files-in-python-like-sql<br>
-Como ordenar una tabla en Python:<br>
 https://www.geeksforgeeks.org/how-to-sort-data-by-column-in-a-csv-file-in-python/<br>

El resto de cosas que he aplicado son cosas que aprendí durante el desarrollo de mi proyecto en Python en la universidad.


