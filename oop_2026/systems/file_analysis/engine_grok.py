import os
from typing import Any

from dotenv import load_dotenv
from loguru import logger
from xai_sdk import Client
from xai_sdk.chat import user, file

from oop_2026.systems.file_analysis.engine import FileAnalysisEngine


class GrokEngine(FileAnalysisEngine):

    def __init__(self, key: str = None, model="grok-4-1-fast-non-reasoning"):
        load_dotenv()
        self.model = model
        if key is None:
            self.key = os.getenv("XAI_KEY")
        else:
            self.key = key
        self.uploaded_files: dict[str, Any] = {}
        self.client = None

    def init_client(self):
        self.client = Client(api_key=self.key)
        logger.info("Client initialized")

    def upload_file(self, file_name) -> str:
        with open(file_name, "rb") as f:
            pdf_bytes = f.read()

        logger.info(f"Uploading {file_name}")
        uploaded_file = self.client.files.upload(pdf_bytes, filename=file_name)
        logger.info(f"Uploaded {file_name}")
        self.uploaded_files[uploaded_file.id] = uploaded_file.id
        return uploaded_file.id

    def analyze(self, prompt: str, file_id: str) -> str:
        logger.info("Starting chat")
        chat = self.client.chat.create(model=self.model)

        logger.info(f"Appending to chat")
        chat.append(user(prompt, file(file_id)))

        logger.info(f"Reading response")
        # ↓↓ this takes 8s
        resp = chat.sample()
        logger.info(f"Finished chat")
        return resp.content
