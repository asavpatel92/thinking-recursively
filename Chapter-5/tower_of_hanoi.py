#===============================================================================
# this function generates the steps to solve the tower of hanoi problem.
#===============================================================================

def moveTower(no_of_disk, start, finish, temp):
    if( no_of_disk == 1 ):
        print "move disk from : %s to %s" %(start, finish)
    else:
        moveTower(no_of_disk - 1, start, temp, finish)
        print "move disk from : %s to %s" %(start, finish)
        moveTower(no_of_disk - 1, temp, finish, start)
        
def moveTower2(no_of_disk, start, finish, temp):
    if ( no_of_disk > 0):
        moveTower(no_of_disk - 1, start, temp, finish)
        print "move disk from : %s to %s" %(start, finish)
        moveTower(no_of_disk - 1, temp, finish, start)
    
def main():
    moveTower(int(raw_input("Enter the number of disks:")), "A", "B", "C")
    moveTower2(int(raw_input("Enter the number of disks:")), "A", "B", "C")

if __name__ == '__main__' :
    main()