import os
from django.http import JsonResponse

def health(request):
    env = os.environ.get("APP_ENV", "dev")
    version = os.environ.get("APP_VERSION", "unknown")
    return JsonResponse({"status": "ok", "env": env, "version": version})