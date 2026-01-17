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
    fid = engine.upload_file(file_name='docker.pdf')

    prompt = f"""
    Ask 10 "seed questions" related to the attached document. 
    Each should be rooted in the document but can venture a little from its content, 
    in order to check the good understanding of document's contepts by the person answering them (called client). 
    Clients are at the level of 2nd year university students, and the questions should reflect this.
    Each of the questions should require a 2-3 sentence answer, 
    and will be a basis for a followup question (which will take into account client's answer). 
    The answer to the seed question and the followup question will be a basis for (your) evaluation 
    of client's understanding of the concepts from the document. Translate your questions to polish. 
    Output seed questions only as a python list in a json with key "questions"."""

    resp = engine.analyze(prompt=prompt, file_id=fid)
    print(f'output:\n{resp}')
