from pathlib import Path


def load_prompt():
    prompt_path = Path(__file__).resolve().parent / "prompts" / "summarize.txt"
    return prompt_path.read_text()


def create_prompt(question):
    template = load_prompt()
    return template.replace("{question}", question)


question = "What is machine learning?"

prompt = create_prompt(question)

print("Generated Prompt:")
print(prompt)