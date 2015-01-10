#===============================================================================
# this function generates the subsets of a given set
#===============================================================================

def findSubsets(l):
    if len(l) == 1:
        return [l]
    if len(l) == 0:
        return []
    res = []
    subsets = findSubsets(l[0:-1])
    res = res+subsets
    res.append([l[-1]])
    for sub in subsets:
        res.append(sub+[l[-1]])
    return res
    
        
            
def main():
    li = list(raw_input("Enter the list without spaces:"))
    print findSubsets(li) 
    
if __name__ == '__main__':
    main()

                