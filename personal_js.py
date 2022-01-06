import json

with open("personal_info.json", "r") as jw:
    a = json.loads(jw.read())

    for item in a["data"]:
        print(item)
        for i in item["family"]["pets"]:
            print(i["name"])
    
    
    b = a.get("data")
    for i in range(len(b)):
        if "family" in b[i].keys():
            c = (b[i].get("family"))
            print(f"Keys : {c.keys()}")
            print(f"Values : {c.values()}")
            print("===============================")
        else:
            print("Nothing")
    
    
    # for i in range (len(b)):
    #     print((b[i]).items())
    #     print((b[i]).keys())
    #     print((b[i]).values())
    
    # for i in range(len(b)):
    #     print((b[i]).get("name"))
    
    
