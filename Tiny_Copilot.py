from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Example choices:
# model_name = "microsoft/CodeGPT-small-py"     # (Garbage Output)
model_name = "Salesforce/codegen-350M-multi"    # (Working - Tested)
# model_name = "Salesforce/codegen-2B-multi"    # (Too slow | Too large for 12GB GPU?)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

# Ensure a pad token exists (tie it to EOS)
if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token

def generate_code(prompt: str,
                  max_tokens: int = 150,
                  do_sample: bool = True,
                  top_p: float = 0.95,
                  temperature: float = 0.8) -> str:

    # Tokenize + pad
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True
    ).to(device)

    # Generate
    outputs = model.generate(
        input_ids=inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_new_tokens=max_tokens,
        do_sample=do_sample,
        top_p=top_p,
        temperature=temperature,
        pad_token_id=tokenizer.eos_token_id
    )
    """outputs = model.generate(
        input_ids=inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_new_tokens=max_tokens,
        do_sample=do_sample,
        top_p=0.9,
        top_k=50,
        temperature=0.3,
        repetition_penalty=1.1,
        no_repeat_ngram_size=3,
        pad_token_id=tokenizer.eos_token_id
    )"""

    # Strip off the prompt
    gen_tokens = outputs[0][inputs.input_ids.shape[-1]:]
    return tokenizer.decode(gen_tokens, skip_special_tokens=True)

if __name__ == "__main__":
    print("Welcome to Tiny Copilot (code edition). Type ‘exit’ to quit.\n")
    try:
        while True:
            user_prompt = input(">>> ")
            if user_prompt.strip().lower() == "exit":
                print("Goodbye!")
                break

            completion = generate_code(user_prompt)
            print(completion)
            print("-" * 60)
    except KeyboardInterrupt:
        print("\nInterrupted. Bye!")