class Logger:
    def __init__(self):
        self.logs = []

    def log(self, level, message):
        entry = f"[{level.upper()}] {message}"
        self.logs.append(entry)

    def info(self, message):
        self.log("info", message)

    def error(self, message):
        self.log("error", message)

    def show_logs(self):
        for log in self.logs:
            print(log)


# Example
logger = Logger()
logger.info("System started")
logger.error("Something failed")
logger.show_logs()