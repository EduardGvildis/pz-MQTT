# stt-pz-3/broker — MQTT broker (Mosquitto) + test scripts

This folder contains a minimal Eclipse Mosquitto broker setup and simple Python
publisher/subscriber scripts for demonstration.

Quick start (Docker):

1. From this folder run the broker and a client container helper:

```bash
docker compose up -d
```

2. Install Python requirements in the client container (one-time):

```bash
docker compose run --rm mqtt-client pip install -r requirements.txt
```

3. Start a subscriber (in a terminal; it will block and print incoming messages):

```bash
docker compose run --rm mqtt-client python subscribe.py --topic test/topic
```

4. Publish a message from another terminal:

```bash
docker compose run --rm mqtt-client python publish.py --topic test/topic --message "hello from docker"
```

Notes:
- The broker exposes MQTT on `1883` and a websocket listener on `9001`.
- For local testing without Docker, install `paho-mqtt` and run the scripts directly.

Acceptance criteria checklist:

- Broker runs locally in Docker
- Minimal config provided (`mosquitto.conf`)
- Demonstration scripts for Publish/Subscribe included
- Commands above show how to run tests
