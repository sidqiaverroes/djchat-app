# Import necessary modules and classes
from rest_framework import serializers
from .models import Server, Channel


# Define a serializer for the Channel model
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"  # Include all fields from the Channel model


# Define a serializer for the Server model
class ServerSerializer(serializers.ModelSerializer):
    num_members = serializers.SerializerMethodField()  # Custom field for num_members
    channel_server = ChannelSerializer(many=True)  # Serialize related channels
    category = serializers.StringRelatedField()

    class Meta:
        model = Server
        exclude = ("member",)  # Exclude the member field from serialization

    # Custom method to get the num_members field
    def get_num_members(self, obj):
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None

    # Override the to_representation method to conditionally remove num_members
    def to_representation(self, instance):
        data = super().to_representation(instance)
        num_members = self.context.get("num_members")
        if not num_members:
            data.pop("num_members", None)
        return data
