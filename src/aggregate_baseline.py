import pandas as pd

telemetry = pd.read_csv('/home/andres/CAiN_repos/telemetry/0/baseline_no_anomaly.csv')

sorted_telemetry = telemetry.sort_values(['time'])


