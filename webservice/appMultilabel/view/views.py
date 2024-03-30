
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

class Clasificacion():

    @api_view(['GET','POST'])
    def predecir(request):
        if request.method == 'GET':
            try:
                print('****************EMPIEZA *******************************')
                result = "hola mundito"  # Lógica de predicción para el método GET
            except Exception as e:
                result = "Error"  # Lógica de predicción para el método GET 
            finally:
                data = {'result': result}
                return JsonResponse(data)
        