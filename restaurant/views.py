from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu, MenuItem, User
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, "index.html", {})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})


class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})


class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
