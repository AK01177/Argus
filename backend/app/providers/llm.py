import os
from google import genai

class LLMProvider:
    "Base Class"
    def summarize_file(self, file_path: str, cotent: str) -> str:
        raise NotImplementedError("Subclass must implement the parse_file method")

class GeminiProvider(LLMProvider):
    def __init__(self):
        self.client=genai.Client()
        self.model_name="gemini-3.5-flash"

    def summarize_file(self, file_path: str, content: str)-> str:
        prompt=f"""What does this code foo? Give me one sentence answer
        File : {file_path}
        Code : {content}
        """
        response=self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        return response.text.strip()