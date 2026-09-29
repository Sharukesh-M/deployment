from pathlib import Path


def create_prompt(question):
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "summarize.txt"
    template = prompt_path.read_text()
    return template.replace("{question}", question)


question = "What is Artificial Intelligence?"

prompt = create_prompt(question)

assert question in prompt
assert "{question}" not in prompt

print("Prompt test passed!")