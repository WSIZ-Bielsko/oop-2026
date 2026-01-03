"""
Code for analysis of PDF files (and - likely - other files as well).

"""
import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types import FileObject
from loguru import logger

"""
Works with openai provider only (others have other file api).
"""


def get_client() -> OpenAI:
    API_KEY = os.getenv("GPT_KEY")

    client_ = OpenAI(api_key=API_KEY, base_url='https://api.openai.com/v1/')
    return client_


def upload_input_file(client, file_name: str, purpose="batch") -> FileObject:
    """
    :param client:
    :param file_name:
    :param purpose: "batch" or "user_data"
    :return:
    """
    input_file = client.files.create(
        file=open(file_name, "rb"),
        purpose=purpose
    )

    return input_file


if __name__ == '__main__':
    load_dotenv()
    client = get_client()
    logger.info("Uploading file")
    up_file = upload_input_file(client, "faktura.pdf", purpose="user_data")
    print(up_file)
    fid = up_file.id

    keys = ["nr_faktury", "data_wystawienia", "data_sprzedaży", "sprzedawca_nazwa",
            "sprzedawca_nip", "nabywca_nazwa", "nabywca_nip", "razem_brutto",
            "razem_netto"]

    logger.info("Calling GPT")
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": fid,
                    },
                    {
                        "type": "input_text",
                        "text": "Przeanalizuj załączony PDF. "
                                f"Zwróć wyłącznie json z następującymi polami: {keys}",
                    },
                ],
            },
        ],
    )

    print(response.output_text)
