import time
import random
import schedule
from git_push import git_push
from write_file import write_file

def activity_generator():
    rand_commit_amount = random.randint(5, 20)  # Between 5 and 20 commits
    print(f"Executing {rand_commit_amount} commits with a delay of 5 to 27 minutes between commits.\n")
    
    for i in range(rand_commit_amount):
        write_file()
        git_push()
        rand_time_delay = random.randint(5, 27)  # Delay between 5 and 27 minutes
        print(f"Commit {i + 1}/{rand_commit_amount} done. Next commit in {rand_time_delay} minute(s).\n")
        time.sleep(rand_time_delay * 60)  # Convert minutes to seconds

# Schedule the task
schedule.every().day.at("17:44").do(activity_generator)

# Run the scheduler
print("Scheduler started. Waiting for tasks...\n")
while True:
    schedule.run_pending()
    time.sleep(1)
