import json
from kafka import KafkaConsumer

bootstrap_servers = 'pkc-ymrq7.us-east-2.aws.confluent.cloud:9092'
security_protocol = 'SASL_SSL'
sasl_mechanism = 'PLAIN'
sasl_plain_username = 'VFEA4YJF3V2RMNJU'
sasl_plain_password = 'g35bTPWvnO0XZvyrDv+ZTXa4kpvlqz7PWzNOsuKQpKIJwD7/mAHRQ8zHAoYcZcUQ'

topic = 'Test'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_plain_username=sasl_plain_username,
    sasl_plain_password=sasl_plain_password,
    sasl_mechanism=sasl_mechanism,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

try:
    for message in consumer:
        key = message.key
        value = message.value

        print(f'Received message: key={key}, value={value}')
except KeyboardInterrupt:
    pass

consumer.close()
