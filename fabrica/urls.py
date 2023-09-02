from rest_framework import routers
from .views import GrupoViewSet,ProjetoViewSet

router = routers.DefaultRouter()
router.register(r'Projeto', ProjetoViewSet)
router.register(r'Grupo', GrupoViewSet)
urlpatterns = router.urls