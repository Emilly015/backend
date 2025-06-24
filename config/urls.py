from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet, CidadeViewSet, AlunosViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'alunos', AlunosViewSet)
router.register(r'cidade', CidadeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
