
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from appMultilabel.logic.prediccion_modelo import PrediccionModelo
from django.shortcuts import render
import base64
from io import BytesIO
from PIL import Image

class Clasificacion():

    def solicitud(request):
        return render(request, "solicitud.html")

    @api_view(['GET','POST'])
    def test(request):
        if request.method == 'GET':
            try:
                print('**************** TEST *******************************')
                result = "ok"  # Lógica de predicción para el método GET
            except Exception as e:
                result = "Error"  # Lógica de predicción para el método GET 
            finally:
                data = {'result': result}
                return JsonResponse(data)

    @api_view(['GET', 'POST'])
    def predecirIOJson(request):
        try:
            print('**************** PREDECIR ******************************')

            # Obtener los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)
            path = data.get('path')

            # Crear una instancia de la clase PrediccionModelo
            modelo = PrediccionModelo()

            # Llamar al método predecirImagen() en la instancia del modelo
            result = modelo.predecirImagen(path)
        except Exception as e:
            result = f'Error: {e}'  # Lógica de predicción para el método GET
        finally:
            data = {'result': result}
            return JsonResponse(data)

    @api_view(['GET', 'POST'])
    def predecir(request):
        try:
            #Formato de datos de entrada
            path_imagen = request.POST.get('path_imagen')

            # Crear una instancia de la clase PrediccionModelo
            modelo = PrediccionModelo()

            # Llamar al método predecirImagen() en la instancia del modelo
            result = modelo.predecirImagen(path_imagen)
        except Exception as e:
            result = f'Error: {e}'  # Lógica de predicción para el método GET

        return render(request, "informe.html",{"e":result})

    @api_view(['GET', 'POST'])
    def predecirConImagen(request):
        try:
            print('**************** PREDECIR  CON IMAGEN ******************************')

            # Obtener los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)
            image_b64 = data.get('imageData')
            print('******** INICIO IMAGEDATA******')
            print(image_b64)
            print('******** FIN IMAGEDATA *****')
            # Decodificar la imagen base64 en una representación de imagen
            image_bytes = base64.b64decode(image_b64)
            image = Image.open(BytesIO(image_bytes))
            
            # Crear una instancia de la clase PrediccionModelo
            modelo = PrediccionModelo()

            # Llamar al método predecirImagen() en la instancia del modelo
            result = modelo.predecirConImagen(image)
        except Exception as e:
            result = f'Error: {e}'  # Lógica de predicción para el método GET
        finally:
            data = {'result': result}
            return JsonResponse(data)