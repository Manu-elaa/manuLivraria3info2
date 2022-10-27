from rest_framework.serializers import ModelSerializer

from core.models import Autor
from core.models import Categoria
from core.models import Editora
from core.models import Livro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"