from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    CursoAPIView,
    AvaliacaoAPIView,
    CursosAPIView,
    AvaliacoesAPIView,
    CursosViewSet,
    AvaliacoesViewSet,
)

router = SimpleRouter()
router.register('cursos', CursosViewSet)
router.register('avaliacoes', AvaliacoesViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),

    path('curso/<int:pk>', CursoAPIView.as_view(), name='curso'),

    path('curso/<int:curso_pk>/avaliacoes/',
         AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),

    path('curso/<int:curso_pk>/avaliacao/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(), name='curso_avaliacao'),


    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),

]
