import json



class Question:
    def __init__(self,question,answers,total):
        self.question = question
        self.total = total
        self.answers = answers


def func2Read(fName="Oprosnik"):
    L = []
    with open(fName,encoding="utf8") as f:
        l = json.loads(f.read())
        #[print(d.items()) for d in l for k,v in d.items()]
        for d in l:
            k,v = list(d.items())[0]
            question = Question(k,v,list(d.items())[1][1])
            L.append(question)
    return L

def funcQuiz(L):
    listRes=[]
    i=0
    while i < len(L):
        print("\n"+L[i].question,end="\n\n")
        numbAnswer=0
        for a in L[i].answers.keys():
            numbAnswer += 1
            print(str(numbAnswer)+") " + a)
        try:
            num = [int(x)-1 for x in input("enter a response number or a comma separated number: ").split(",")]
            if min(num) < 0 or max(num) > numbAnswer-1:
                continue
        except Exception:
            continue
        listRes.append(num)
        #print(listRes)
        #print("\t\tnext question\n")
        i += 1
    return listRes

def func2():
    L = func2Read()
    listRes = funcQuiz(L)
    i = 0
    lenght = len(listRes)
    print("\n\n\nyour answers")
    stringRes = ''
    sumRes = 0
    sumMax = 0
    while i < lenght:
        stringQuesch = "\n"+L[i].question
        sumMax += L[i].total
        stringRes += stringQuesch+"\n"
        print(stringQuesch)
        right = set()
        boo = False
        for t in listRes[i]:
            tupl = list(L[i].answers.items())[t]
            sumRes+=tupl[1]
            print("\t"+tupl[0])
            stringRes += "\t"+tupl[0]+"\n"
            if tupl[1] <= 0:
                boo = True
        if boo:
            print("right answers")
            [print("\t\t", t[0]) for ind, t in enumerate(L[i].answers.items()) if t[1] > 0 and ind not in listRes[i]]
            #if tupl[1] <= 0 or  :
        i+=1
    stringRes+="\nMaximum points: "+ str(sumMax)+"\n"
    stringRes+="You scored points: "+str(sumRes)
    #print(stringRes)

    with open("OprosnikRes","w",encoding="utf8") as f:
        f.write(stringRes)
    print("Maximum points: "+ str(sumMax),"You scored points: "+str(sumRes),sep="\n")
func2()