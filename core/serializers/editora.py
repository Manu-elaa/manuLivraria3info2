from rest_framework.serializers import ModelSerializer

from core.models import Autor
from core.models import Categoria
from core.models import Editora
from core.models import Livro

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
