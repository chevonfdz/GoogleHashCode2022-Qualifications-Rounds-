def get_data(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            print(lines)

            count = 0
            conDict = {}

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

            # for line in range(1, len(lines)):
            #     likes = lines[line].strip().split()

            print(count)
            print(conDict)

            f.close()

    except FileNotFoundError:
        return "File not found"


file = "a_an_example.in.txt"
conNum = 0
proNum = 0
get_data(file)
print("------")
