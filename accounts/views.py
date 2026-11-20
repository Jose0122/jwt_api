from rest_framework.views import APIView
from .serializers import RegisterSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                "message":"User registered successfully"
            },
            status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response(
            {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            }
        )

class AdminDataView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({
            "message": "Welcome Admin!",
            "username": request.user.username
        })

