import time
import random
import schedule
from git_push import git_push
from write_file import write_file

def activity_generator():
    # Generate random values for each execution
    rand_commit_amount = random.randint(1, 100)
    rand_time_delay = random.randint(1, 60)
    print(f"Executing {rand_commit_amount} commits with a delay of {rand_time_delay} seconds.")
    
    for _ in range(rand_commit_amount):
        write_file()
        git_push()
        time.sleep(rand_time_delay)

# Schedule the task at midnight
schedule.every().day.at("17:26").do(activity_generator)

# Run the schedule loop
print("Scheduler started. Waiting for tasks...")
while True:
    schedule.run_pending()
    time.sleep(1)
