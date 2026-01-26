from abc import ABC, abstractmethod
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
import uvicorn
from loguru import logger

from oop_2026.systems.map_storage.storage_dict_and_list import DictStorage

# FastAPI app
app = FastAPI()
storage = DictStorage()


class SetItemRequest(BaseModel):
    key: str
    value: Any


@app.get("/items/{key}")
def get_item(key: str):
    try:
        return {"value": storage[key]}
    except KeyError:
        raise HTTPException(status_code=404, detail="Key not found")


@app.post("/items")
def set_item(request: SetItemRequest):
    logger.info(f"Setting {request.key} to {request.value}")
    storage[request.key] = request.value
    return {"status": "ok"}


@app.get("/length")
def get_length():
    return {"length": len(storage)}


@app.get("/keys")
def get_keys():
    return {"keys": list(storage.keys())}


@app.delete("/clear")
def get_keys():
    storage.clear()
    logger.info("Cleared storage")
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5007)
