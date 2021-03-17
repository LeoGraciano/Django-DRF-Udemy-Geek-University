from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = '__all__'

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError(
            'A avaliação precisa ser uma nota de 1 a 5')


class CursoSerializer(serializers.ModelSerializer):

    """
    # Nested Relationship - ele é bom um para um
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    """

    # HyperLinked Related Field - Acessa penas link utilizando no Restfull
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,  # só para Leitura
        view_name='avaliacao-detail'
    )
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = '__all__'

    def get_media_avaliacoes(self, obj):
        # AVG uma função do django que faz calculo de media e returna o resultado no no avaliacao__avg
        media = obj.avaliacoes.aggregate(
            Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media*2)/2

    # # Primary Key Related Field - forma mais performatica
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
