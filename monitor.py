import time

def monitor_logs(file_path):

    with open(file_path, "r") as file:

        file.seek(0, 2)

        while True:

            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            if "ERROR" in line:
                print("ALERT:", line.strip())