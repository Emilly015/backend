from rest_framework.serializers import ModelSerializer
from .models import Estado, Alunos, Cidade

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'
