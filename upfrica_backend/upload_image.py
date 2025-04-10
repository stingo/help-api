from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.conf import settings
from uuid import uuid4
import os

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_image(request):
    image = request.FILES.get('image')
    if not image:
        return Response({"error": "No image provided"}, status=400)

    # ✅ Optional: Validate content type
    if image.content_type not in ['image/jpeg', 'image/png', 'image/webp']:
        return Response({"error": "Only JPEG, PNG, or WEBP allowed"}, status=400)

    # ✅ Optional: Limit file size (e.g. max 5MB)
    if image.size > 5 * 1024 * 1024:
        return Response({"error": "Image too large (max 5MB)"}, status=400)

    # ✅ Ensure unique filename
    ext = os.path.splitext(image.name)[-1]
    filename = f"{uuid4().hex}{ext}"
    path = default_storage.save(f'uploads/help-center/{filename}', image)

    image_url = f'{settings.MEDIA_URL}{path}'
    return Response({"url": image_url})