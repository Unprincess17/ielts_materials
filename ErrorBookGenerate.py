import datetime
import os

#get file from last commit
Files = os.popen("git diff --name-only HEAD HEAD^").read().split("\n")
#get time as MONTH-DAY
time = datetime.datetime.now().strftime("%m%d")
for file in Files:
    os.system(f"diff -y --suppress-common-lines ref/{file} test/{file} > err/{file}.{time}.txt")
# os.system(f"git add err && git commit -m \"update {time}'s error books\" && git push")