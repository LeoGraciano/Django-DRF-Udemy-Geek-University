from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import EhSuperUser
from .models import Curso, Avaliacao

from django.shortcuts import get_list_or_404

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


class CursosAPIView(generics.ListCreateAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return generics.get_object_or_404(self.queryset, curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return generics.get_object_or_404(self.queryset, pk=self.kwargs.get('avaliacao_pk'))


class CursosViewSet(viewsets.ModelViewSet):
    permission_classes = [
        EhSuperUser,
        permissions.DjangoModelPermissions
    ]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # Não existe paginação de decorate ela é feita manual, terai que ser feito manualmente a logica
        self.pagination_class.page_size = 2  # numero de elemento que quero paginar
        # pegando avalição pelo PK do curso
        avalicoes = Avaliacao.objects.filter(curso_id=pk)
        # criando a lista de objetos filtrados
        page = self.paginate_queryset(avalicoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avalicoes, many=True)
        return Response(serializer.data)


class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
