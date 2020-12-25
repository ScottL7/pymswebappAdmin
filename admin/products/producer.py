import json
import pika

params = pika.URLParameters('amqps://ifqrcxlo:SzpuVN4LtaoCFpHaWd6RAyqgoqLLWgGM@finch.rmq.cloudamqp.com/ifqrcxlo')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
