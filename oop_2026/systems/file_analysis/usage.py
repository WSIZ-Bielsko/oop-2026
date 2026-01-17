from dotenv import load_dotenv
from loguru import logger

from oop_2026.systems.file_analysis.engine_gemini import GeminiEngine
from oop_2026.systems.file_analysis.engine_gpt import GptEngine
from oop_2026.systems.file_analysis.engine_grok import GrokEngine

if __name__ == '__main__':
    load_dotenv()

    # engine = GrokEngine()  # 9s/query
    # engine = GeminiEngine()  # 2s/query
    engine = GptEngine(model='gpt-5-mini-2025-08-07')  # 3s/query (gpt-4.1)
    engine.init_client()
    fid = engine.upload_file(file_name='faktura.pdf')
    logger.info(f'Uploaded file [{fid}]')
    nip = engine.analyze('Analyze file and retrieve "nip_sprzedawcy"; '
                         'return only the parsed value in a json with single field',
                         file_id=fid)
    print(f'nip sprzedawcy = {nip}')
