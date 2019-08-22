
from rest_framework import serializers

from I_listen_app.models import ListenSingle, Download


class ListenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListenSingle
        fields = '__all__'

class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'