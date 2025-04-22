from django.urls import path
from gpt_integration.views import GetGPTResponseView

urlpatterns = [
    path("api/v1/get", GetGPTResponseView.as_view(), name="get_gpt_response"),
]
