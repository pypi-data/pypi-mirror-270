from promptflow import tool

@tool
def get_greeting_message(input_text: str, **kwargs) -> str:
	for key, value in kwargs.items():
		print(f"Key {key}'s value is {value}")
	return len(kwargs)