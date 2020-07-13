import psutil
import eventador as ev
import time
import json
import socket

def gather_telemetry(session):

    hostname=socket.gethostname()
    fqdn=socket.getfqdn()
    ip_address = socket.gethostbyname(hostname)


    while True:

        payload = {"cpu_stats": psutil.cpu_stats(),
                   "cpu_times": psutil.cpu_times(),
                   "load_avg": psutil.getloadavg(),
                   "hostname": hostname,
                   "fqdn": fqdn,
                   "ip_address": ip_address
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
