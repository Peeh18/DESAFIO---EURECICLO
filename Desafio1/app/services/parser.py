from lxml import etree
from app.models.article import Article

def parse_xml_file(path):
    try:
        # Lê e analisa o arquivo XML
        tree = etree.parse(path)
        root = tree.getroot()

        # Pega a tag 'article' do XML
        article_tag = root.find("article")
        body_tag = article_tag.find("body") if article_tag is not None else None

        return Article(
            id=article_tag.get("id"),
            name=article_tag.get("name"),
            idOficio=article_tag.get("idOficio"),
            pubName=article_tag.get("pubName"),
            artType=article_tag.get("artType"),
            pubDate=article_tag.get("pubDate"),
            artClass=article_tag.get("artClass"),
            artCategory=article_tag.get("artCategory"),
            artSize=article_tag.get("artSize"),
            artNotes=article_tag.get("artNotes"),
            numberPage=article_tag.get("numberPage"),
            pdfPage=article_tag.get("pdfPage"),
            editionNumber=article_tag.get("editionNumber"),
            highlightType=article_tag.get("highlightType"),
            highlightPriority=article_tag.get("highlightPriority"),
            highlight=article_tag.get("highlight"),
            highlightimage=article_tag.get("highlightimage"),
            highlightimagename=article_tag.get("highlightimagename"),
            idMateria=article_tag.get("idMateria"),
            identifica=body_tag.findtext("Identifica") if body_tag is not None else None,
            data=body_tag.findtext("Data") if body_tag is not None else None,
            ementa=body_tag.findtext("Ementa") if body_tag is not None else None,
            titulo=body_tag.findtext("Titulo") if body_tag is not None else None,
            subtitulo=body_tag.findtext("SubTitulo") if body_tag is not None else None,
            texto=body_tag.findtext("Texto") if body_tag is not None else None
        )
    except Exception as e:
        print(f"Erro ao processar o arquivo {path}: {e}")
        return None