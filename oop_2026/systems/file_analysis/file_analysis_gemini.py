import os

from dotenv import load_dotenv
from google import genai
from google.genai import types, Client
import pathlib

from google.genai.types import Part


# https://ai.google.dev/gemini-api/docs/document-processing


def get_client() -> Client:
    GEMINI_KEY = os.getenv("GEMINI_KEY")
    client_ = genai.Client(api_key=GEMINI_KEY)
    return client_


def get_prompt():
    keys = ["nr_faktury", "data_wystawienia", "data_sprzedaży", "sprzedawca_nazwa",
            "sprzedawca_nip", "nabywca_nazwa", "nabywca_nip", "razem_brutto",
            "razem_netto"]

    prompt = "Summarize this document extracting a json with following keys: " + ", ".join(keys) + "."
    return prompt


def simple(client):
    # Retrieve and encode the PDF byte
    filepath = pathlib.Path('faktura.pdf')

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=filepath.read_bytes(),
                mime_type='application/pdf',
            ),
            get_prompt()])
    print(response.text)


def large(client):
    # proper way to call gemini in a reusable way

    # Retrieve and encode the PDF byte
    file_path = pathlib.Path('faktura.pdf')

    # Upload the PDF using the File API
    sample_file = client.files.upload(
        file=file_path,
    )
    print(sample_file)
    prompt = get_prompt()

    # for subsequent calls
    file_uri = sample_file.uri
    file_mime = sample_file.mime_type
    file_part = Part.from_uri(file_uri=file_uri, mime_type=file_mime)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[file_part, prompt])
    print(response.text)


"""
name='files/xzon6ed70yo9' display_name=None mime_type='application/pdf' size_bytes=28530 create_time=datetime.datetime(2026, 1, 3, 10, 27, 43, 294782, tzinfo=TzInfo(UTC)) expiration_time=datetime.datetime(2026, 1, 5, 10, 27, 42, 866141, tzinfo=TzInfo(UTC)) update_time=datetime.datetime(2026, 1, 3, 10, 27, 43, 294782, tzinfo=TzInfo(UTC)) sha256_hash='YmE3OTJlNTVkMmJhMzEzMzdhOWQ0OWVkMzY0YzYwMzA4NTAzZThkMWYxOTc3MTRmNzhjMzA1NmI3ZWEyNWZmMw==' uri='https://generativelanguage.googleapis.com/v1beta/files/xzon6ed70yo9' download_uri=None state=<FileState.ACTIVE: 'ACTIVE'> source=<FileSource.UPLOADED: 'UPLOADED'> video_metadata=None error=None
"""

if __name__ == '__main__':
    load_dotenv()
    client = get_client()
    # simple(client)
    large(client)
