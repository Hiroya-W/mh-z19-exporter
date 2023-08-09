import time

import mh_z19
from prometheus_client import Gauge, start_http_server

co2_metric = Gauge("MH_Z19_EXPORTER_CO2", "CO2 concentration in ppm")

if __name__ == "__main__":
    start_http_server(9000)
    while True:
        res = mh_z19.read()
        co2_metric.set(res["co2"])
        time.sleep(1)
