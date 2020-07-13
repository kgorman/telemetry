# telemetry
A system stats and telemetry generator for Eventador Platform

## Setup and configuration

Install requirements:
```
pip install -r requirements.txt
```

Set environment:
```BASH
export URL=<<PRODUCER URL FROM EVENTADOR>>
export TOPIC="telemetry"
export API_KEY=<<API_KEY FROM EVENTADOR>>
```

You can get your URL and API_KEY at https://eventador.cloud

## Running

```
python telemetry.py
```
