from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola desde Django  con Moli")


def despedida(request):
    return HttpResponse("Asta Luego desde Django  con Moli")  

def fecha(request):
    fecha_actual = datetime.datetime.now()

    documento="""

    Fecha y hora actuales %s
    
    """ % fecha_actual

    return HttpResponse(documento) 

def calculaEdad(request,edad, agno):
    
    periodo=agno-2021
    edadFutura=edad+periodo
    documento="En el año %s tendras %s años" %(agno, edadFutura)
    return HttpResponse(documento)
