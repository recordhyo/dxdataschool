origin = "ABCDECGGCCGKEDCGGCGGCCDDDDGCCGCCGSIEJWCGGCCGCSLK"
cnt = origin.count("GCCG")
answer = []
for i in range(cnt) :
    answer.append(origin.find("GCCG"))
    origin = origin.replace("GCCG","****",1)
print(answer)
