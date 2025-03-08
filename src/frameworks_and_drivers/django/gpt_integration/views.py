from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from frameworks_and_drivers.django.gpt_integration.gpt_service import generate_post_content

class GeneratePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response({"error": "Prompt is required"}, status=400)
        
        try:
            content = generate_post_content(prompt)
            return Response({"content": content}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
