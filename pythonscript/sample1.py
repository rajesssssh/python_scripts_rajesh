mydict={
"name": "Rajesh",
"id": 111,
"domain": ["devops", "cloud engineer", "SRE"],
"tools": {"os": ["linux", "windows"], "cloud": "aws"}
}
print(mydict)
print(mydict["id"])
print(mydict["name"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["domain"][2])
print(mydict["tools"]["os"])
print(mydict["tools"]["os"][1])
