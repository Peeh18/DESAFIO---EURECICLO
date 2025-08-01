import pika
import json
from app.models.article import Article

def publish_article(article: Article):
    try:
        # Conecta ao RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Garante que o exchange existe
        channel.exchange_declare(exchange='publicacoes', exchange_type='topic')

        # Publica o artigo como JSON
        channel.basic_publish(
            exchange='publicacoes',
            routing_key='artigo.extraido',
            body=json.dumps(article.dict())
        )

        connection.close()
    except Exception as e:
        print(f"Erro ao publicar artigo: {e}")