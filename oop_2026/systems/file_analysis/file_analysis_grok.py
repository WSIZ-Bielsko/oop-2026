import os

from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, file
from loguru import logger

load_dotenv()


def get_client() -> Client:
    key = os.getenv("XAI_KEY")
    client_ = Client(api_key=key)
    return client_


if __name__ == '__main__':
    load_dotenv()
    client = get_client()
    file_name = "faktura.pdf"

    with open(file_name, "rb") as f:
        pdf_bytes = f.read()

    # upload file to x.ai
    logger.info(f"Uploading {file_name}")
    uploaded_file = client.files.upload(pdf_bytes, filename=file_name)
    print(uploaded_file)
    logger.info(f"Uploaded {file_name}")



    # chat = client.chat.create(model="grok-4-fast")
    logger.info("Starting chat")
    chat = client.chat.create(model="grok-4-1-fast-non-reasoning")

    keys = ["nr_faktury", "data_wystawienia", "data_sprzedaży", "sprzedawca_nazwa",
            "sprzedawca_nip", "nabywca_nazwa", "nabywca_nip", "razem_brutto",
            "razem_netto"]

    logger.info(f"Appending to chat")
    chat.append(user(f"Przeanalizuj tekst, podaj odczytaj następujące wartości: {keys}; zwróć json-a z tymi wartościami",
                     file(uploaded_file.id)))

    # cost = ~1.5 cent/pdf-call, grok-4-1-fast-non-reasoning

    logger.info(f"Reading response")
    # ↓↓ this takes 8s
    resp = chat.sample()
    print(resp.content)  # proper json
    logger.info(f"Finished chat")

    # cleanup
    client.files.delete(uploaded_file.id)
