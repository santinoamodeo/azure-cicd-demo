import os
from django.http import JsonResponse

def health(request):
    env = os.environ.get("APP_ENV", "dev")
    
    version = "unknown"
    env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env_version")
    if os.path.exists(env_file):
        with open(env_file) as f:
            version = f.read().strip().replace("APP_VERSION=", "")

    return JsonResponse({"status": "ok", "env": env, "version": version})