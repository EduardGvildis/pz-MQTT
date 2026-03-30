#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqtt

def main():
    parser = argparse.ArgumentParser(description='MQTT publisher')
    parser.add_argument('--host', default='broker', help='MQTT broker host')
    parser.add_argument('--port', type=int, default=1883, help='MQTT broker port')
    parser.add_argument('--topic', required=True, help='Topic to publish to')
    parser.add_argument('--message', required=True, help='Message payload')
    parser.add_argument('--qos', type=int, default=0, help='QoS level')
    args = parser.parse_args()

    client = mqtt.Client()
    client.connect(args.host, args.port, 60)
    client.publish(args.topic, args.message, qos=args.qos)
    client.disconnect()
    print(f"Published '{args.message}' to {args.topic} (qos={args.qos})")

if __name__ == '__main__':
    main()
