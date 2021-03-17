from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['pk']

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    """
    Avalização
    """
    curso = models.ForeignKey(
        'Curso', related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comentario = models.TextField(max_length=255)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = _("Avaliação")
        verbose_name_plural = _("Avaliações")
        unique_together = ['email', 'curso']
        ordering = ['pk']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.email} com a nota {self.avaliacao}'
