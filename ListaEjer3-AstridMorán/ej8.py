def ejercicio8():
    import re
    texto="Python es uno de los lenguajes de programación dinámicos más populares que existen entre los que se encuentran Java, Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje scripting, es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples scripts, hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y testing de aplicaciones "
    
    encontrado = re.search("Python",  texto)
    if encontrado:
        print("Se ha encontrado la palabra:", encontrado)
    else:
        print("No se ha encontrado la palabra:", encontrado)

ejercicio8()