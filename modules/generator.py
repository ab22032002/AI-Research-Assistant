"""
Module: generator.py
Purpose: Generate context-aware responses using Flan-T5.
"""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

class FlanT5Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        print(f"[INFO] Loading {model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_answer(self, query, context, temperature=0.2, max_new_tokens=256):
        prompt = f"Answer the question based on context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = self.model.generate(
            **inputs,
            do_sample=False,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
        )
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer
