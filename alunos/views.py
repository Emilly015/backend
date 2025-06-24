from rest_framework.viewsets import ModelViewSet
from .models import Estado, Alunos, Cidade
from .serializers import EstadoSerializer, AlunosSerializer, CidadeSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class AlunosViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
