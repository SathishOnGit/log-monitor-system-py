import csv


class ReportGenerator:

    @staticmethod
    def generate_csv(data):

        with open(
            "reports/log_report.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                ["INFO", "WARNING", "ERROR"]
            )

            writer.writerow([
                data["INFO"],
                data["WARNING"],
                data["ERROR"]
            ])

        print("CSV Report Created")