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

if __name__ == '__main__' :
    print collectN(1000, 1, 0)
