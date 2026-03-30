#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print('Connected with result code', rc)
    client.subscribe(userdata['topic'], qos=userdata.get('qos', 0))

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}")

def main():
    parser = argparse.ArgumentParser(description='MQTT subscriber')
    parser.add_argument('--host', default='broker', help='MQTT broker host')
    parser.add_argument('--port', type=int, default=1883, help='MQTT broker port')
    parser.add_argument('--topic', required=True, help='Topic to subscribe to')
    parser.add_argument('--qos', type=int, default=0, help='QoS level')
    args = parser.parse_args()

    userdata = {'topic': args.topic, 'qos': args.qos}
    client = mqtt.Client(userdata=userdata)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(args.host, args.port, 60)
    client.loop_forever()

if __name__ == '__main__':
    main()
