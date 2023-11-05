# Import necessary modules and classes
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from drf_spectacular.utils import extend_schema

from .schema import server_list_docs
from .models import Server, Category
from .serializer import ServerSerializer, CategorySerializer


class CategoryListViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


# Define a class for the ServerListViewSet
class ServerListViewSet(viewsets.ViewSet):
    # Initialize the queryset with all Server objects
    queryset = Server.objects.all()
    # permission_classes = [IsAuthenticated]

    # Define a method for listing servers
    @server_list_docs
    def list(self, request):
        """
        List servers based on query parameters.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A serialized response containing the list of servers based on query parameters.

        Raises:
            AuthenticationFailed: If user authentication is required and not authenticated.
            ValidationError: If server with specified ID is not found or if there's a value error.

        This method lists servers based on query parameters such as category, quantity, user filtering,
        the inclusion of the number of members, and filtering by server ID. It returns a response
        containing the serialized server data based on the specified parameters.

        - `category`: Filters servers by the specified category name.
        - `qty`: Limits the number of servers in the response.
        - `by_user`: Filters servers by the requesting user.
        - `with_num_members`: Includes the number of members for each server.
        - `by_serverid`: Filters servers by the specified server ID.

        When `by_serverid` is provided, the method raises a `ValidationError` if the server with the
        specified ID is not found. If user authentication is required and not authenticated, an
        `AuthenticationFailed` exception is raised.

        The method also uses the `ServerSerializer` to serialize the queryset and returns the
        serialized data as a response.
        """

        # Extract query parameters
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # Check if user authentication is required
        # if by_user or (by_serverid and not request.user.is_authenticated):
        #     raise AuthenticationFailed()

        # Filter the queryset by category if specified
        if category:
            self.queryset = self.queryset.filter(category__name=category)

        # Filter the queryset by the requesting user if by_user is specified
        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()

        # Annotate the queryset with the number of members if with_num_members is specified
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        # Limit the queryset to a specific quantity if qty is specified
        if qty:
            self.queryset = self.queryset[: int(qty)]

        # Filter the queryset by a specific server ID if by_serverid is specified
        if by_serverid:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                # Raise an error if the server with the specified ID is not found
                if not self.queryset.exists():
                    raise ValidationError(
                        detail=f"Server with id {by_serverid} not found"
                    )
            except ValueError:
                raise ValidationError(detail="Server with id value error")

        # Serialize the queryset with the ServerSerializer
        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )

        # Return the serialized data as a response
        return Response(serializer.data)
