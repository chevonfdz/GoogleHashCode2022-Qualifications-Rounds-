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
                conName = lines[count].strip().split()[0]
                conSkillCount = lines[count].strip().split()[1]

                for y in range(int(conSkillCount)):
                    count += 1
                    conSkill = lines[count].strip().split()[0]
                    conSkillLvl = lines[count].strip().split()[1]

                    skillDict[conSkill] = conSkillLvl

                conDict[conName] = skillDict

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

    except FileNotFoundError:
        return "File not found"


file = "a_an_example.in.txt"
conNum = 0
proNum = 0
get_data(file)
print("------")
