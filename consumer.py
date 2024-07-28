import pika


def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")


connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)
channel = connection.channel()

channel.queue_declare(queue='letterbox')
channel.basic_consume(queue='letterbox', auto_ack=True,
                      on_message_callback=on_message_received)
print("Start Consuming")
channel.start_consuming()
