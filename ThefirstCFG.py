
def process_input(File):
    list = []
    for line in File:
        line = line.split("\n")
        list.append(line)

    for i in range(len(list)):
        if list[i][-1] == '':
            del list[i][-1]

    f_list = []
    for i in range(len(list)):
        f_list.append(list[i][0])

    f_list = [s.replace('->', '') for s in f_list]
    f_list = [s.replace('*', '') for s in f_list]
    f_list = [s.replace('_', '') for s in f_list]

    return f_list

def main_process(f_list):
    number = int(f_list[0])
    alphabet = f_list[1]
    alphabet = alphabet.split(",")
    transition = []
    noTransition = []
    
    for i in range(4,len(f_list)):
        var = f_list[i].split(",")
        if var[3] != "" :
            transition.append(f_list[i])
        else:
            noTransition.append(f_list[i])

    f_list_of_CFG = []
    for l in range(number):
        if l == 0:
            for i in range(len(transition)):
                var = transition[i].split(",")
                String = ""
                String = String + str(var[0])
                String = String + str(var[2])
                String = String + str(var[4])
                f_list_of_CFG.append(String)
                for j in range(number-1):
                    String = ""
                    String = String.join(var[1])
                    f_list_of_CFG.append(String)
                    for m in range(0,number):

                        String = ""
                        if len(var[3])>1:
                            String = String.join(str("("+var[0]+str(var[3][0])+"q"+str(m)+")"+"("+"q"+str(m)+str(var[3][1])+var[4]+")"))
                        else:
                            String = String.join(str("(" + var[0] + str(var[3][0]) + "q" + str(m) + ")"))
                        f_list_of_CFG.append(String)
        else:
            for i in range(len(transition)):
                var = transition[i].split(",")
                String = ""
                String = String + str(var[0])
                String = String + str(var[2])
                String = String + "qf"
                f_list_of_CFG.append(String)
                for j in range(number - 1):
                    String = ""
                    String = String.join(var[1])
                    f_list_of_CFG.append(String)
                    for m in range(0, number):
                        String = ""
                        if (len(var[3]) > 1):
                            String = String.join(str(
                                "(" + var[0] + str(var[3][0]) + "q" + str(m) + ")" + "(" + "q" + str(m) + str(
                                    var[3][1]) + "qf" + ")"))
                        else:
                            String = String.join(str(
                                "(" + var[0] + str(var[3][0]) + "q" + str(m) + ")"))

                        f_list_of_CFG.append(String)


    others = Other_transition(noTransition)
    for i in range(len(others)):

        f_list_of_CFG.append(others[i])
    return f_list_of_CFG

def Other_transition(lst):
    CFG = []
    for i in range(len(lst)):
        string = ""
        Var = lst[i].split(",")
        string = string + str(Var[0])
        string = string + str(Var[2])
        string = string + str(Var[4])
        string = string + " -> "
        if Var[1] != "":
            string = string + str(Var[1])
        else:
            string = string + "_"

        CFG.append(string)
    return CFG





def main():
    input_file = input("Please Enter The File Dir \n")
    input_file = open(input_file , 'r')
    proceture = process_input(input_file)
    Main_list = main_process(proceture)

    for i in range(4*int(proceture[0])):
        print(Main_list[0] + " -> " + Main_list [1] + Main_list[2] + " | " + Main_list[1] + Main_list[3])
        for j in range(2*int(proceture[0])):
            del Main_list[0]

    for i in range(len(Main_list)):
        print(Main_list[i])





if __name__ == "__main__":
    main()