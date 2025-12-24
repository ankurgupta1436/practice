from datetime import datetime
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print('task completed')
    print()
first_name = 'susan'
print_time(first_name)