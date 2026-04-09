import requests

payload = {
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "prompt": "Explain KV cache in one paragraph.",
    "max_tokens": 128,
}
print('Example request payload for a vLLM-compatible server:')
print(payload)
print('Replace the URL below with your local vLLM endpoint if available.')
print('requests.post("http://localhost:8000/generate", json=payload)')
