class FileAnalysisEngine:

    def init_client(self):
        pass

    def upload_file(self, file_name) -> str:
        """Uploads a file to the AI server and returns its ID."""

    def analyze(self, prompt, file_id) -> str:
        """Executes a prompt using info from file uploaded earlier."""


class AiClientError(Exception):
    pass