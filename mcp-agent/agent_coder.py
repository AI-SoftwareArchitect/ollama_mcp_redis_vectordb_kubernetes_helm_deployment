import subprocess

def generate_code_with_ollama(prompt: str, model: str = "deepseek-coder:latest") -> str:
    result = subprocess.run(
        ["ollama", "run", model, prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout
