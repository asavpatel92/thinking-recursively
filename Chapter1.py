# problem 1
def collectN(n, p, x): 
    print "collecting %d from %d people" % (n, p)
    # if it get's down to $1, then return $1 * number_of_people
    if n == 1:
        return 1 * p

    # else keep dividing the amount and multiplying number of people
    x += collectN(n / 10, p * 10, x)
    return x

# exercise 1.1
# for this exercise just replace 10 with 5 in above solution

# exercise 1.3
# this is a generic solution will work with any N number of coins
def split_seq(seq, size):
        newseq = []
        splitsize = 1.0 / size * len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i * splitsize)):int(round((i + 1) * splitsize))])
        return newseq
    
def findCounterfeit(coins):
    if len(coins) == 1:
        print "counterfeit is %s" % (coins[0])
    else:
        chunk1 = split_seq(coins, 3)[0]
        chunk2 = split_seq(coins, 3)[1]
        chunk3 = split_seq(coins, 3)[2]
        if (len(chunk1) == len(chunk2) == len(chunk3)):
            if (sum(chunk1) > sum(chunk2) or sum(chunk3) > sum(chunk2)):
                print "counterfeit must be in chunk2"
                print chunk2
                findCounterfeit(chunk2)
            elif (sum(chunk1) > sum(chunk3)):
                print "counterfeit must be in chunk3"
                print chunk3
                findCounterfeit(chunk3)
            else:
                print "counterfeit must be in chunk1"
                print chunk1
                findCounterfeit(chunk1)
        else:
            if (len(chunk1) == len(chunk2)):
                if (sum(chunk1) > sum(chunk2)):
                    print "counterfeit must be in chunk2"
                    print chunk2
                    findCounterfeit(chunk2)
                else:
                    print "counterfeit must be in chunk1"
                    print chunk1
                    findCounterfeit(chunk1)
            elif (len(chunk1) == len(chunk3)):
                if (sum(chunk1) > sum(chunk3)):
                    print "counterfeit must be in chunk3"
                    print chunk3
                    findCounterfeit(chunk3)
                else:
                    print "counterfeit must be in chunk1"
                    print chunk1
                    findCounterfeit(chunk1)
            else:
                print "counterfeit must be in chunk2"
                print chunk2
                findCounterfeit(chunk2)

if __name__ == '__main__' :
    print collectN(1000, 1, 0)
    # "coins" is a list of Weights of coins
    coins = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    findCounterfeit(coins)
    
