from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Produto
from .serializers import ProdutoSerializer

import json

@api_view(['GET'])
def get_produtos(request):

    if request.method == 'GET':

        produtos = Produto.objects.all()

        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

#INICIO DO CRUD 

@api_view(['GET', 'PUT'])
def get_id(request, id):

    try:
        produto =Produto.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    
#EDITANDO DADOS (PUT)
    
    if request.method == 'PUT':

        serializer = ProdutoSerializer(produto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

#CRUDZAO 

@api_view (['GET', 'POST', 'PUT', 'DELETE'])
def produto_manager(request):

#BUSCANDO DADOS (GET)

    if request.method == 'GET':
        try:
            if request.GET['produto']:
                id = request.GET['produto']
                try:
                    produto = Produto.objects.get(pk=id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = ProdutoSerializer(produto)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

#CRIANDO DADOS (POST)

    if request.method == 'POST':
        novo_produto = request.data
        serializer = ProdutoSerializer(data=novo_produto)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

#DELETAR DADOS (DELETE)

    if request.method == 'DELETE':
        try:
            produto_to_delete = Produto.objects.get(pk=request.data['id'])
            produto_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


'''#EDITANDO DADOS (PUT)

    if request.method == 'PUT':

        produto = request.data['id']

        update_produto = Produto.objects.get(pk=produto)

        serializer = ProdutoSerializer(update_produto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
;        return Response(status=status.HTTP_400_BAD_REQUEST) '''
