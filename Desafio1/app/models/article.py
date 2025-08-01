from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    # Atributos da tag <article>
    id: Optional[str]
    name: Optional[str]
    idOficio: Optional[str]
    pubName: Optional[str]
    artType: Optional[str]
    pubDate: Optional[str]
    artClass: Optional[str]
    artCategory: Optional[str]
    artSize: Optional[str]
    artNotes: Optional[str]
    numberPage: Optional[str]
    pdfPage: Optional[str]
    editionNumber: Optional[str]
    highlightType: Optional[str]
    highlightPriority: Optional[str]
    highlight: Optional[str]
    highlightimage: Optional[str]
    highlightimagename: Optional[str]
    idMateria: Optional[str]

    # Campos dentro da tag <body>
    identifica: Optional[str]
    data: Optional[str]
    ementa: Optional[str]
    titulo: Optional[str]
    subtitulo: Optional[str]
    texto: Optional[str]