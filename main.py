import time
import random
import schedule
from git_push import git_push
from write_file import write_file

def activity_generator():
    # Generate random commit amount
    rand_commit_amount = random.randint(5, 20)
    print(f"Executing {rand_commit_amount} commits with a delay of 1 to 8 hours between commits.")
    
    for i in range(rand_commit_amount):
        write_file()
        git_push()
        rand_time_delay = random.randint(5, 27)  # Delay between 5 and 27 minutes
        print(f"Commit {i + 1}/{rand_commit_amount} done. Next commit in {rand_time_delay} hour(s).")
        time.sleep(rand_time_delay * 60)  # Convert minutes to seconds

# Schedule the task at a specific time
schedule.every().day.at("17:43").do(activity_generator)

# Run the schedule loop
print("Scheduler started. Waiting for tasks...")
while True:
    schedule.run_pending()
    time.sleep(1)
