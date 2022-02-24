def get_data(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            print(lines)

            count = 0
            conDict = {}
            proDict = {}

            conNum = lines[count].strip().split()[0]
            proNum = lines[count].strip().split()[1]

            print(conNum, proNum)

            for x in range(int(conNum)):
                count += 1
                skillDict = {}
                conTime = 0
                conName = lines[count].strip().split()[0]
                conSkillCount = lines[count].strip().split()[1]

                for y in range(int(conSkillCount)):
                    count += 1
                    conSkill = lines[count].strip().split()[0]
                    conSkillLvl = lines[count].strip().split()[1]

                    skillDict[conSkill] = conSkillLvl

                conDict[conName] = [conTime, skillDict]

            print(count)
            print(conDict)

            for x in range(int(proNum)):
                count += 1
                skillDict = {}
                proName = lines[count].strip().split()[0]
                proNoDate = lines[count].strip().split()[1]
                proScore = lines[count].strip().split()[2]
                proBestBefore = lines[count].strip().split()[3]
                proSkillCount = lines[count].strip().split()[4]

                for y in range(int(proSkillCount)):
                    count += 1
                    proSkill = lines[count].strip().split()[0]
                    proSkillLvl = lines[count].strip().split()[1]

                    skillDict[proSkill] = proSkillLvl

                proDict[proName] = [proNoDate, proScore, proBestBefore, skillDict]

            print(count)
            print(proDict)

            f.close()

        return conDict,proDict

    except FileNotFoundError:
        return "File not found"


def set_contributors():
    global proDict
    global conDict

    for projectName in proDict:
        setProj = []
        project = proDict[projectName]
        setProj.append(projectName)

        for projectSkill in project[3]:
            skill = projectSkill
            skillLvl = project[3].get(projectSkill)

            for conName in conDict:
                conSkills = conDict[conName]

                for conSkill in conSkills[1]:
                    if skillLvl < conSkills[1].get(conSkill) and conSkills[0] <= project[0]+conSkills[0]:
                        setProj.append(conName)
                        conSkills[0] = project[0] + conSkills[0]
                    elif skillLvl == conSkills[1].get(conSkill) and conSkills[0] <= project[0]+conSkills[0]:
                        setProj.append(conName)
                        conSkills[0] = project[0] + conSkills[0]
                        conSkills[conSkill] = conSkills.get(conSkill) + 1
                    elif skillLvl - 1 == conSkills[1].get(conSkill):
                        for conName2 in conDict:
                            conSkills2 = conDict[conName2]

                            for conSkill2 in conSkills2[1]:
                                if skillLvl < conSkills2[1].get(conSkill2) and conSkills[0] <= project[0]+conSkills[0]:
                                    setProj.append(conName)
                                    setProj.append(conName2)
            print(setProj)


file = "a_an_example.in.txt"
# conNum = 0
# proNum = 0

conDict, proDict = get_data(file)
print("Data Retrieved\n-------------\n")

set_contributors()
