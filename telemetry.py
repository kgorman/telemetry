import psutil
import eventador as ev
import time
import json

def gather_telemetry(session):

    while True:

        payload = {"cpu_stats": psutil.cpu_stats(),
                   "cpu_times": psutil.cpu_times(),
                   "load_avg": psutil.getloadavg()
                   }
        payload = json.loads(json.dumps(payload)) # normalize structures
        try:
            ev.produce(session, payload)
        except Exception as ex:
            print("unable to produce {}".format(ex))

        time.sleep(60)

if __name__== "__main__":
    try:
        session  = ev.create_session()
        response = ev.create_topic(session)
        gather_telemetry(session)
    except Exception as e:
        print(e)
