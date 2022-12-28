from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from APP.models import MASSAGE

class CraetSerislizer(ModelSerializer):

    class Meta:
        model = MASSAGE
        fields = [

            'receiver',
            'subject',
            'massage',
        ]