Examen Magneto MercadoLibre

1) El código fuente se encuentra en este repositorio de GitHub. El mismo pertenece a un proyecto realizado en Django. Los puntos 1, 2 y 3 se encuentra en este mismo proyecto

2) El proyecto se encuentra hosteado en https://test-django-280915.rj.r.appspot.com (A través de Google Cloud)

3) La API tiene dos urls para su consumo según pedido del ejercicio: 

https://test-django-280915.rj.r.appspot.com/api/mutant/ 
https://test-django-280915.rj.r.appspot.com/api/stats/

La primera requiere pasarle en el body el json correspondiente al dna. Si lo prueban con PostMan, configurar el content-type en application/json.
La primera permite solo POST, ejemplo del body:

{
	"dna":["AACW","CACT","CCAC","CAAV"]
}

Como resultado, puede devolver un http 200, un 403 o un 500. Siendo un 200 para un dna de mutante. un 403 para dna humano y un 500 para un error en la aplicación no controlado.
Un error 403 también puede darse cuando los parámetros no son correctos. Validando, por ejemplo, una variable dna a recibir de tipo lista, una lista no vacía, una matriz NxN, etc.

La segunda url se puede consumir por GET y devuelve, ejemplo:

{"count_mutant_dna": 2, "count_human_dna": 6, "ratio": 0.3333333333333333}

4) EL programa tiene una serie de test unitarios ubicados en el archivo tests.py (dentro de la aplicación API). Ahí también se puede ver como ejecutar el programa, creando una instancia de la clase Person.

5) Consideraciones extra, pensamiento de ejercicio, se permiten combinaciones verticales, horizontales y diagonales, tanto para "adelante" como para "atrás". 
Ejemplo:
TTGC
ATCA
CCTG
CAAT

En este caso tenemos las dos diagonales, la del 0,0 de la T y la del 0,3 de la C, esta última invertida.
Por otro lado, cuando se superan las máximas combinaciones de la secuencia, en este caso 4, consideré otra combinación distinta.
Ejemplo:
TTTTT
QWERT
ASDFG
ZXCVB
VBNMM

Este caso va a dar verdadero, ya que tenemos una combinación de 4 "T" que es la posición: (0,0),(0,1),(0,2),(0,3) y otra combinación que es: ((0,1),(0,2),(0,3),(0,4). Al ser listas de pares distintas, yo consideré como dos secuencias distintas. Por ende, para el caso mencionado, tenemos más de una secuencia de 4 letras iguales. Tal como indica el enunciado

6) Dejé dos urls más para que puedan usar:

https://test-django-280915.rj.r.appspot.com/api/clearDB/
https://test-django-280915.rj.r.appspot.com/api/list2/

La primera borra la base de ADNs verificados, por si quieren limpiarla para hacer pruebas
La segunda devuelve un listado de los ADNs consultados, con el resultado de si es o no mutante.

