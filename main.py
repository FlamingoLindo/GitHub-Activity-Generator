import time
import random
import schedule
from git_push import git_push
from write_file import write_file

def activity_generator():
    rand_commit_amount = random.randint(5, 20)
    print(f"Executing {rand_commit_amount} commits with a delay of 5 to 27 minutes between commits.\n")
    
    for i in range(rand_commit_amount):
        write_file()
        git_push()
        rand_time_delay = random.randint(5, 27)
        print(f"Commit {i + 1}/{rand_commit_amount} done. Next commit in {rand_time_delay} minute(s).\n")
        time.sleep(rand_time_delay * 60)

schedule.every().day.at("09:00", 'America/Sao_Paulo').do(activity_generator)

print("Scheduler started. Waiting for tasks...\n")
while True:
    schedule.run_pending()
    time.sleep(1)
