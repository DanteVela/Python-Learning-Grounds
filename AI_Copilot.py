# sample: a tiny “Copilot” using OpenAI’s API or an open LLM
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1) load model (change to any open-source checkpoint)
model_name = "gpt2-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 2) simple function to complete code
def complete_code(prompt: str, max_tokens=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        top_p=0.95,
        temperature=0.8
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 3) test it
if __name__ == "__main__":
    user_prompt = """
    # Function to compute Fibonacci numbers
    def fib(n):
    """
    print(complete_code(user_prompt))