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

Como resultado, puede devolver en http 200, un 403 o un 500. Siendo un 200 para un dna de mutante. un 403 para dna humano y un 500 para un error en la aplicación.
Un error 403 también puede darse cuando los parámetros no son correctos. Validando, por ejemplo, una variable a recibir de tipo lista, una lista no vacía, una matriz NxN, etc.

La segunda url se puede consumir por GET y devuelve, ejemplo:

{"count_mutant_dna": 2, "count_human_dna": 6, "ratio": 0.3333333333333333}

4) EL programa tiene una serie de test unitarios ubicados en el archivo tests.py (dentro de la aplicación API). Ahí también se puede ver como ejecutarlo

5) Consideraciones extra, pensamiento de ejercicio, url extra
