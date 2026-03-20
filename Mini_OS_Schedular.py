class Process:
    def __init__(self, pid, burst, priority):
        self.pid = pid
        self.burst = burst
        self.remaining = burst
        self.priority = priority


class Scheduler:
    def __init__(self, quantum):
        self.quantum = quantum
        self.queue = []

    def add_process(self, process):
        self.queue.append(process)

    def run(self):
        time = 0

        # Sort by priority (lower = higher priority)
        self.queue.sort(key=lambda p: p.priority)

        while self.queue:
            process = self.queue.pop(0)

            run_time = min(self.quantum, process.remaining)
            print(f"P{process.pid} runs for {run_time}")

            process.remaining -= run_time
            time += run_time

            if process.remaining > 0:
                self.queue.append(process)

        print("Total execution time:", time)


# Demo
scheduler = Scheduler(2)
scheduler.add_process(Process(1, 5, 1))
scheduler.add_process(Process(2, 3, 0))  # higher priority
scheduler.add_process(Process(3, 4, 2))

scheduler.run()