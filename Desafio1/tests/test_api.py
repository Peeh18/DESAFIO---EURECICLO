from app.services.parser import parse_xml_file
from app.models.article import Article
import tempfile

# Exemplo de XML 
XML_DE_EXEMPLO = """
<xml>
  <article id="123" name="Exemplo" pubDate="2025-01-01">
    <body>
      <Identifica><![CDATA[Ministério do Exemplo]]></Identifica>
      <Data><![CDATA[2025-01-01]]></Data>
      <Texto><![CDATA[Este é um artigo de teste.]]></Texto>
    </body>
  </article>
</xml>
"""

def test_parse_xml_file():
    # Cria um arquivo XML temporário com o conteúdo acima
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".xml", delete=False, encoding="utf-8") as tmp:
        tmp.write(XML_DE_EXEMPLO)
        tmp.seek(0)
        caminho = tmp.name

    artigo = parse_xml_file(caminho)

    
    assert isinstance(artigo, Article)
    assert artigo.id == "123"
    assert artigo.name == "Exemplo"
    assert artigo.pubDate == "2025-01-01"
    assert artigo.identifica == "Ministério do Exemplo"
    assert artigo.texto == "Este é um artigo de teste."