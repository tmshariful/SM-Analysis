import os
import json
from tqdm import tqdm
import csv
from datetime import datetime 

directory = "messages/inbox"
folders = os.listdir(directory)

if ".DS_Store" in folders:   #for mac
    folders.remove(".DS_Store")

for folder in tqdm(folders):
    print(folder)
    for filename in os.listdir(os.path.join(directory,folder)):
        if filename.startswith("message"):
            data = json.load(open(os.path.join(directory,folder,filename), "r"))
            for message in data["messages"]:
                try:
                    date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
                    sender = message["sender_name"]
                    content = message["content"]
                    print (date , "  ", sender, "   ",   content, '\n')
                    with open("output.csv", 'w', encoding="utf-8" ) as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow([date,sender,content])

                except KeyError:
                    pass