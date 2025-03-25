from django.urls import path
from frameworks_and_drivers.django.gpt_integration.views import GetGPTResponseView


urlpatterns = [
    path("api/v1/get", GetGPTResponseView.as_view(), name="get_gpt_response"),
]
