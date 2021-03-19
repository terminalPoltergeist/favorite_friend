with open("data.txt", "r+") as fp:
    lines = fp.readlines()
    ross = 0
    rachel = 0
    chandler = 0
    monica = 0
    joey = 0
    phoebe = 0
    for i in lines:
        lines[lines.index(i)] = i.replace("\n", "")
    for i in lines:
        if "Ross" in i:
            ross += 1
        elif "Rachel" in i:
            rachel += 1
        elif "Chandler" in i:
            chandler += 1
        elif "Monica" in i:
            monica += 1
        elif "Joey" in i:
            joey += 1
        elif "Phoebe" in i:
            phoebe += 1
    print("Phoebe: ", phoebe, "Joey: ", joey, "Monica: ", monica,
          "Chandler: ", chandler, "Rachel: ", rachel, "Ross: ", ross)
fp.close()
