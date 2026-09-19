import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
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

    def embed_text(self, text:str) -> list[float]:
        try:
            result= self.client.models.embed_content(
                model="gemini-embedding-001",
                contents=text,
                config=types.EmbedContentConfig(output_dimensionality=768)
            )
            return result.embeddings[0].values
        except Exception as e:
            print(f"Embedding Failed: {e}")
            return [0.0] * 768

    def answer_question(self, question:str, context_chunks: list[str]) -> str:
        context_text= "\n\n---\n\n".join(context_chunks)

        prompt=f"""
        You are a senior software engineer helping a teammate to understand the codebase.

        Here is the relevant code from the repository:
        {context_text}

        Answer the following question based ONLY on the code above. If the code doesn't
        contain the answer, say "I dont have the enough context to answer that."

        Question : {question}
        """

        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
            )
            return response.text

        except Exception as e:
            print(f"Failed to generate answer : {e}")
            return "Sorry I ran into an error generating the answer."