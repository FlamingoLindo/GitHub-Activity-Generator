import os
import time

def git_push():
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    os.system('git add .')
    os.system(f'git commit -m "{date}"')
    os.system('git push')
    print("\nGit push done")