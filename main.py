from analyzer import LogAnalyzer
from report_generator import ReportGenerator
from search import search_logs
from threading import Thread
from monitor import monitor_logs
from threading import Thread
from monitor import monitor_logs
from logger_config import logger

log_file = "logs/app.log"


thread = Thread(
    target=monitor_logs,
    args=("logs/app.log",)
)

thread.daemon = True
thread.start()

analyzer = LogAnalyzer(log_file)

result = analyzer.analyze()

print("\nLOG SUMMARY")
print("-" * 30)

print("INFO:", result["INFO"])
print("WARNING:", result["WARNING"])
print("ERROR:", result["ERROR"])

print("\nERROR DETAILS")

for error in result["ERRORS"]:
    print(error)

logger.info("Application Started")

search_logs("logs/app.log", "database")

ReportGenerator.generate_csv(result)
