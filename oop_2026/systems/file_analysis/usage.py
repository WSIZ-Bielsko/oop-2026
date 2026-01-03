from oop_2026.systems.file_analysis.engine import GrokEngine
from loguru import logger

if __name__ == '__main__':
    engine = GrokEngine()
    # engine = GeminiEngine()
    engine.init_client()
    fid = engine.upload_file(file_name='faktura.pdf')
    logger.info(f'Uploaded file [{fid}]')
    nip = engine.analyze('Analyze file and retrieve "nip_sprzedawcy"; '
                         'return only the parsed value in a json with single field',
                         file_id=fid)
    print(f'nip sprzedawcy = {nip}')

