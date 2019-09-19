import os
import json

print("start")
with open("treejson.json","r") as infile:
    with open("treejson_noSingleEl.json","w+") as output:
        for line in infile:
            # lin = json.loads(line)
            # print(lin)
            print(line)
            if "SingleElectron" in line:
                continue
            output.write(line)



