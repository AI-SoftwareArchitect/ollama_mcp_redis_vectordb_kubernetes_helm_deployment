import requests
from redis_client import get_context_from_redis

AGENT_CODER_URL = "http://localhost:8080/agent-coder"

def generate_command(user_input: str) -> str:
    context = get_context_from_redis("project_context") or ""
    command = f"Kullanıcı şöyle dedi: '{user_input}'. Mevcut proje bilgisi: '{context}'. Buna göre API veya HTML/CSS kodu üret."

    # Komutu Agent Coder'a gönder
    response = requests.post(AGENT_CODER_URL, json={"prompt": command})

    if response.status_code == 200:
        return response.json().get("code", "Kod üretilemedi.")
    else:
        return f"Hata oluştu: {response.status_code} - {response.text}"
