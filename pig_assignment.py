import random

def roll():
    return random.randint(1,6)

def pigTurn(target = 20, score = 0):
    turnTotal = 0
    rolledOne = False
    while turnTotal < target and turnTotal+score < 100 and not rolledOne:
        dice =  roll()
        #print("Roll:", dice)
        if dice == 1:
            turnTotal = 0
            rolledOne = True
        else:
            turnTotal += dice
    #print("Turn total:", turnTotal)
    return turnTotal

def holdAt20Sims(trials):
    results = {0:0}
    results[20] = 0
    results[21] = 0
    results[22] = 0
    results[23] = 0
    results[24] = 0
    results[25] = 0

    for _ in range(trials):
        turnTotal = pigTurn()
        results[turnTotal] += 1
    print("Turn total\tEstimated Prob")
    for turnTotal in results:
        print(turnTotal,results[turnTotal]/trials,sep="\t\t")

def holdAtXSims(trials, target = 20):
    results = {0:0}
    for i in range(6):
        results[target+i] = 0
    for _ in range(trials):
        turnTotal = pigTurn(target)
        results[turnTotal] += 1
    print("Turn total\tEstimated Prob")
    for turnTotal in results:
        print(turnTotal,results[turnTotal]/trials,sep="\t\t")

def part4Test(score):
    for _ in range(3):
        score =  score + pigTurn(20,score)
        print("Score:",score)
        print()

def solitaireGame(target = 20):
    score = 0
    turns = 0
    while score < 100:
        score =  score + pigTurn(target , score)
        turns += 1
        #print("Score:",score)
        #print()
    return turns

def avgTurns(trials, target = 20):
    totalTurns = 0
    for _ in range(trials):
         totalTurns += solitaireGame(target)
    print(target, totalTurns/trials,sep="\t")

for target in range(5,50):
    avgTurns(1000000,target)