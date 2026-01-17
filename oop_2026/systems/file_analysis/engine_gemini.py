import os
import pathlib

from google import genai
from google.genai import types
from loguru import logger

from oop_2026.systems.file_analysis.engine import FileAnalysisEngine, AiClientError


class GeminiEngine(FileAnalysisEngine):

    def __init__(self, key: str = None, model="gemini-2.5-flash"):
        self.model = model
        if key is None:
            self.key = os.getenv("GEMINI_KEY")
        else:
            self.key = key
        self.client = None
        self.uploaded_files: dict[str, types.File] = {}

    def init_client(self):
        GEMINI_KEY = os.getenv("GEMINI_KEY")
        client_ = genai.Client(api_key=GEMINI_KEY)
        self.client = client_

    def upload_file(self, file_name) -> str:
        if self.client is None:
            raise AiClientError("Client not initialized")

        file_path = pathlib.Path(file_name)

        logger.info(f"Uploading {file_name}")
        file: types.File = self.client.files.upload(file=file_path, )
        logger.info(f"Uploaded {file_name}, uri = {file.uri}")
        self.uploaded_files[file.uri] = file

        # for subsequent calls could do:
        # file_uri = file.uri
        # file_mime = file.mime_type
        # file_part = Part.from_uri(file_uri=file_uri, mime_type=file_mime)
        # and use file_part for calls instead of `file`

        return file.uri

    def analyze(self, prompt, file_id) -> str:
        if file_id not in self.uploaded_files:
            raise AiClientError(f"File {file_id} not uploaded yet")

        file = self.uploaded_files[file_id]
        logger.info(f"Analyzing file {file.name}")
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[file, prompt])
        logger.info(f"Finished analyzing file {file.name}")
        return response.text
