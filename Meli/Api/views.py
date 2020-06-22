import types

from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

from .classes import Person
from .models import DNA


@api_view(['GET'])
def list2(request):
    test=DNA.objects.all()
    data={
        "element" : list(test.values('dna','isMutant'))
    }
    return JsonResponse(data)


@api_view(['GET'])
def clearDB(request):
    DNA.objects.all().delete()
    return Response(status=status.HTTP_200_OK)

@cache_page(60)
@api_view(['GET'])
def stats(request):
    try:
        mutants=DNA.objects.filter(isMutant=True)
        humans=DNA.objects.filter(isMutant=False)
        if(len(humans)>0):
            ratio=(len(mutants)/len(humans))
        else:
            ratio=0

        data={
            "count_mutant_dna" : len(mutants),
            "count_human_dna" : len(humans),
            "ratio" : ratio
        }
        return JsonResponse(data)
    except:
        #AGREGADO DE LOGS CORRESPONDIENTE, NO LO AGREGUÉ PARA SIMPLIFICAR
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@cache_page(60)
@api_view(['POST'])
def mutant(request):

    try:
        #Get data
        postedData= request.data["dna"]
        #check data
        if(str(type(postedData))!="<class 'list'>"):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        #process request
        person = Person()
        result=person.isMutant(postedData)

        #logging request
        if(not DNA.objects.filter(dna=postedData)):
            model = DNA()
            model.dna = postedData
            model.isMutant = result
            model.save()

        #response result
        if(result):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    except:
        #AGREGADO DE LOGS CORRESPONDIENTE, NO LO AGREGUÉ PARA SIMPLIFICAR
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


