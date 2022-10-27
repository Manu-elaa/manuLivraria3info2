from rest_framework.serializers import ModelSerializer

from core.models import Autor
from core.models import Categoria
from core.models import Editora
from core.models import Livro


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1