import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from app.ai.system_prompt import SYSTEM_PROMPT


class AIClient:
    """
    Handles communication with the AI model.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("RAPHAEL_AI_KEY")

        if not api_key:
            raise ValueError(
                "RAPHAEL_AI_KEY is missing from .env"
            )

        self.client = InferenceClient(
            token=api_key
        )

        self.model = "Qwen/Qwen2.5-7B-Instruct"


    def ask(self, prompt: str) -> str:
        """
        Sends a prompt to the AI model.
        """

        response = self.client.chat_completion(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=300,
            temperature=0.3
        )

        return (
            response.choices[0]
            .message
            .content
            .strip()
        )

        return response.strip()