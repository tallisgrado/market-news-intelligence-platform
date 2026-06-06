import requests


def analyze_with_ai(title):
    prompt = f"""
Analise esta manchete financeira:

"{title}"

Responda em português brasileiro, curto e direto.

Retorne exatamente neste formato:

Título Traduzido:

Sentimento:

Impacto Ouro:
Nível Ouro (1-3):

Impacto XAU/USD:
Nível XAU/USD (1-3):

Impacto Bolsas:
Nível Bolsas (1-3):

Impacto Dólar:
Nível Dólar (1-3):

Impacto Bitcoin:
Nível Bitcoin (1-3):

Confiança:

Justificativa:

Regras:
- Traduza o título preservando o sentido financeiro.
- Impacto deve ser Positivo, Negativo ou Neutro.
- Nível 1 = impacto fraco.
- Nível 2 = impacto moderado.
- Nível 3 = impacto forte.
- Considere Fed, juros, inflação, dólar, risco geopolítico e apetite ao risco.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:1.5b",
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        data = response.json()

        return data["response"]

    except requests.exceptions.Timeout:
        return "A IA local demorou demais para responder. Tente novamente ou use um modelo menor."

    except requests.exceptions.ConnectionError:
        return "O Ollama não está ativo. Abra o Ollama antes de executar a análise."

    except Exception as e:
        return f"Erro ao executar análise com IA: {e}"