import config

from openai import OpenAI

GROQ_URL = "https://api.groq.com/openai/v1"

MODELS = getattr(config, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtral-8x7b-32768","openai/gpt-oss-20b"])

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: HF_GROQ_KEY missing in config.py"
    c = OpenAI(api_key=key, base_url=GROQ_URL)

    last_err = None
    for m in MODELS:
        try:
            r = c.chat.completions.create(
                model = m,
                messages = [{"role":"user","content":prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return r.choice[0].message.content
        except Exception as e:
            last_err = e
    return(
        "gro moddel faile.\n"
        f"Tried models:{MODELS}\n"
        "fix:\n"
        "1) switch to hf by importing hhf.py in main.py or\n"
        "2) replace groq moddele in groq.py (gr0q m_models).\n"
        f"dddetails:{type(last_err).__name__}:{last_err}"
    )
