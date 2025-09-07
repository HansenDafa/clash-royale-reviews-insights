# src/sentiment_granite.py
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Ganti model dengan IBM Granite yang sesuai
MODEL_ID = "ibm-granite/granite-3.0-3b-a800m-instruct"

# Load tokenizer & model dari Hugging Face
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto" if torch.cuda.is_available() else None,
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else None,
    trust_remote_code=True
)

# Buat pipeline teks—meski sebenarnya Granite bukan classifier, kita bisa "prompt-engineer" untuk analisis sentiment
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def predict_sentiment_granite(texts):
    """
    texts: string atau list of strings
    return: list of dict berisi 'text' dan 'sentiment'
    """
    if isinstance(texts, str):
        texts = [texts]
    outputs = []
    prompt_template = (
        "Beri label pada teks berikut sebagai positive, negative, atau neutral:\n"
        "Teks: {text}\nLabel:"
    )
    for t in texts:
        prompt = prompt_template.format(text=t)
        gen = generator(prompt, max_new_tokens=10)
        label = gen[0]["generated_text"].split("Label:")[-1].strip().split("\n")[0]
        outputs.append({"text": t, "label": label.lower()})
    return outputs

if __name__ == "__main__":
    contoh = [
        "Game ini seru banget, saya suka!",
        "Pay to win, bikin males main.",
        "Biasa aja, tidak terlalu menarik."
    ]
    print(predict_sentiment_granite(contoh))
