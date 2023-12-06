from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name_or_path = "TheBloke/Llama-2-7b-Chat-GPTQ"
print("[INFO] Loading model from HuggingFace model hub...")
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="cuda")

prompt_template = f"""Write a simple code for website using HTML"""

print("[INFO] Generating response...")
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.1,
    top_p=0.95,
    top_k=40,
    repetition_penalty=1.1,
)

print(pipe(prompt_template)[0]["generated_text"])
