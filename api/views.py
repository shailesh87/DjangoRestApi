from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.serializers import ProductSerializer, AudioProcessingRequestSerializer
from api.services.product_service import create_product, get_all_products
from api.services.audio_service import extract_audio_snippets
import os

class ProductView(APIView):
    @swagger_auto_schema(
        responses={200: ProductSerializer(many=True)},  # Response schema for GET
    )
    def get(self, request):
        products = get_all_products()
        return Response([{
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": str(p.price),
            "created_at": p.created_at
        } for p in products])

    @swagger_auto_schema(
        request_body=ProductSerializer,  # Input schema for POST
        responses={
            201: ProductSerializer,  # Response schema for successful creation
            400: "Bad Request"       # Response schema for errors
        }
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = create_product(serializer.validated_data)
            return Response({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": str(product.price),
                "created_at": product.created_at
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AudioProcessingView(APIView):
    def post(self, request):
        serializer = AudioProcessingRequestSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = request.FILES['audio_file']
            timestamps = serializer.validated_data['timestamps']

            # Save the uploaded audio file temporarily
            temp_audio_file = f"temp_{audio_file.name}"
            with open(temp_audio_file, 'wb') as f:
                for chunk in audio_file.chunks():
                    f.write(chunk)

            try:
                # Call the service to process audio
                snippet_paths = extract_audio_snippets(temp_audio_file, timestamps)

                # Cleanup the temporary audio file
                os.remove(temp_audio_file)

                return Response({"snippets": snippet_paths}, status=status.HTTP_200_OK)

            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
