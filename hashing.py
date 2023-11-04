import random

# rehash is the function that manually doubles the size of our tables
def rehash(currSize, table1, table2):
    currSize = currSize * 2;
    # Manually we are doubling the size of our tables and setting their lengths with 'None' values
    table1 = [None] * currSize
    table2 = [None] * currSize
    return (table1,table2, currSize);

def hashInsert(table1, table2, key, index, loopCount):
    if(table1[index] == [None]):
        table1[index] = key;
    else:
        loopCount += 1;

    return;



class hashInfo:
    randomVar1 = random.randint(1,1000000); # Temporarily bounding random values 1-1m
    randomVar2 = random.randint(1,1000000);
    def hFunc(self, key, listLength, primeValue):
        hashedAddress = ((self.randomVar1 * key + self.randomVar2) % primeValue) % listLength;
        return(key, hashedAddress);

