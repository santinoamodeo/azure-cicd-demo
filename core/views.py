import os
from django.http import JsonResponse

def health(request):
    env = os.environ.get("APP_ENV", "dev")
    return JsonResponse({"status": "ok", "env": env})