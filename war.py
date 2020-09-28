from cards import *
trials = 10000
results=[]
for i in range(trials):

    #deck a and b
    decka=deck()
    deckb=deck()

    #shuffles decks a and b
    decka.shuffle()
    deckb.shuffle()

    # point tally
    ascore = 0
    bscore = 0
    while decka.cardsleft()>0:
        acard1=decka.dealcard() #dealing card for deck a
        bcard1=deckb.dealcard() #dealing card for deck b
        if acard1.value()>bcard1.value(): #2 pts if deck a draw is greater than deck b
            ascore += 2
        if acard1.value()<bcard1.value(): #2 pts if deck b draw is greater than deck a
            bscore += 2
        if acard1.value()== bcard1.value(): #0 pts if deck a draw is greater than deck b
            ascore += 0
            bscore += 0
    if ascore>bscore:
        results.append(ascore-bscore)
    if ascore<bscore:
        results.append(bscore-ascore)
    if ascore==bscore:
        results.append(ascore-bscore)
for i in range(0,54,2):
    print (i,results.count(i)/trials)
