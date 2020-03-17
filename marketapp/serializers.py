from rest_framework.serializers import ModelSerializer

from marketapp.models import Tovar, Sklad, Postavschik, Postavka


class TovarSerializer(ModelSerializer):
    class Meta:
        model = Tovar
        fields = '__all__'

class SkladSerializer(ModelSerializer):
    class Meta:
        model = Sklad
        fields = '__all__'

class PostavschikSerializer(ModelSerializer):
    class Meta:
        model = Postavschik
        fields = '__all__'

class PostavkaSerializer(ModelSerializer):
    class Meta:
        model = Postavka
        fields = '__all__'