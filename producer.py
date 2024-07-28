import pika

connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)
channel = connection.channel()
channel.queue_declare(queue="letterbox")
message = ["Hello1 this is Subhash",
           "Hello2 this is Subhash", "Hello3 this is Subhash", "Hello4 this is Subhash", "Hello5 this is Subhash"]
for i in message:
    channel.basic_publish(exchange='', routing_key="letterbox", body=i)
# message = "Hello2 this is Subhash"
# message = "Hello3 this is Subhash"
# message = "Hello4 this is Subhash"
# message = "Hello5 this is Subhash"


print(f"sent message:{message}")
connection.close()
