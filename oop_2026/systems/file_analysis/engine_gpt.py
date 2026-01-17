import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from openai.types import FileObject
from loguru import logger

from oop_2026.systems.file_analysis.engine import FileAnalysisEngine, AiClientError


class GptEngine(FileAnalysisEngine):

    def __init__(self, key: str = None, model="gpt-4.1"):
        self.model = model
        if key is None:
            self.key = os.getenv("GPT_KEY")
        else:
            self.key = key
        self.client = None
        self.uploaded_files: dict[str, FileObject] = {}

    def init_client(self):
        API_KEY = os.getenv("GPT_KEY")
        try:
            client_ = OpenAI(api_key=API_KEY, base_url='https://api.openai.com/v1/')
        except OpenAIError as e:
            raise AiClientError(f"Failed to initialize client: {e}")
        self.client = client_

    def upload_file(self, file_name) -> str:
        if self.client is None:
            raise AiClientError("Client not initialized")

        logger.info(f"Uploading {file_name}")
        purpose = "user_data"
        file: FileObject = self.client.files.create(
            file=open(file_name, "rb"),
            purpose=purpose
        )
        logger.info(f"Uploaded {file_name}")
        self.uploaded_files[file.id] = file

        return file.id

    def analyze(self, prompt, file_id) -> str:
        if file_id not in self.uploaded_files:
            raise AiClientError(f"File {file_id} not uploaded yet")

        logger.info(f"Analyzing file {file_id}")
        response = self.client.responses.create(
            model="gpt-4.1",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_file",
                            "file_id": file_id,
                        },
                        {
                            "type": "input_text",
                            "text": prompt,
                        },
                    ],
                },
            ],
        )
        logger.info(f"Finished analyzing file {file_id}")
        return response.output_text
