class LogAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path

    def analyze(self):
        info_count = 0
        warning_count = 0
        error_count = 0

        errors = []

        with open(self.file_path, "r") as file:

            for line in file:

                if "INFO" in line:
                    info_count += 1

                elif "WARNING" in line:
                    warning_count += 1

                elif "ERROR" in line:
                    error_count += 1
                    errors.append(line.strip())

        return {
            "INFO": info_count,
            "WARNING": warning_count,
            "ERROR": error_count,
            "ERRORS": errors
        }