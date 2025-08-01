from fastapi import APIRouter, UploadFile, File
import tempfile
from app.services.extractor import extract_zip
from app.services.parser import parse_xml_file
from app.messaging.publisher import publish_article
from app.storage import artigos_extraidos

router = APIRouter()

@router.post("/upload/")
async def upload_zip(file: UploadFile = File(...)):
    # Salva o arquivo .zip temporariamente
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        zip_path = tmp.name

    # Extrai o conteúdo do arquivo XML do .zip
    xml_files = extract_zip(zip_path)
    artigos = []

    # Processa cada arquivo XML
    for xml in xml_files:
        artigo = parse_xml_file(xml)
        if artigo:
            artigo.origem_zip = file.filename
            artigos.append(artigo)
            artigos_extraidos.append(artigo)
            publish_article(artigo)
        
    return {"message": f"{len(artigos)} artigos enviados com sucesso."}

@router.get("/artigos/")
def listar_artigos():
    return artigos_extraidos