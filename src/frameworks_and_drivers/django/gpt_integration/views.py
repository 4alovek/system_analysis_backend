from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from frameworks_and_drivers.django.gpt_integration.gpt_service import GPTService
from django.http import JsonResponse
from django.views import View

class GetGPTResponseView(View):
    def get(self, request, *args, **kwargs):
        gpt_service = GPTService()
        response_text = gpt_service.generate_post_content()
        return JsonResponse({"response": response_text})
