from dotenv import load_dotenv

load_dotenv()
from typing import Union

import requests
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.logger import logger

from middlewares import validate_api_key
from models import Address, AddressInput, FileUrlInput, Invoice
from services.invoices import parse_address, parse_invoice
from validators.common import validate_file

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/parse/invoice", dependencies=[Depends(validate_api_key)])
def parse_invoice_route(file: UploadFile) -> Invoice:
    if not file:
        raise HTTPException(status_code=400, detail="file is required")

    is_valid_file = validate_file(file.content_type, file.size)
    if not is_valid_file:
        raise HTTPException(status_code=400, detail="Invalid file")

    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(file.file.read())

    return parse_invoice(temp_file_path)


@app.post("/parse/invoice/url", dependencies=[Depends(validate_api_key)])
def parse_invoice_url_route(file_url: FileUrlInput) -> Invoice:
    input_file_url = str(file_url.file_url)

    temp_file_path = f"/tmp/{input_file_url.split('/')[-1]}"
    with requests.get(input_file_url) as r:
        with open(temp_file_path, "wb") as f:
            f.write(r.content)

    if not file_url.file_url:
        raise HTTPException(status_code=400, detail="file url is required")

    return parse_invoice(temp_file_path)


@app.post("/parse/address", dependencies=[Depends(validate_api_key)])
def parse_address_route(address: AddressInput) -> Address:
    try:
        return parse_address(address.address)
    except Exception as e:
        logger.error("Error parsing address", exc_info=e)
        raise HTTPException(status_code=500, detail="Error parsing address")
