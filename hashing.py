import random

# rehash is the function that manually doubles the size of our tables
def rehash(currSize):
    currSize = currSize * 2;
    # Manually we are doubling the size of our tables and setting their lengths with 'None' values
    table1 = [None] * currSize
    table2 = [None] * currSize
    return (table1, table2);

# hashInsert parameters are our two tables, our key value, the hashed index of our key, and the current number of
# iterations in the current attempted insert
def hashInsert(table1, table2, key, index, loopCount, maxLoop):
    loopCount += 1;
    if(maxLoop != loopCount):
        if(table1[index] == [None]):    # If the index is empty from a rehash or from initial creation we can simply insert the value
            table1[index] = key;
        else:
            hashInsert(table2, table1, table1[index], index, loopCount, maxLoop);  # If the index isn't empty we recursively call hashInsert again swapping the table we are inserting to as well as the value we are trying to insert
            table1[index] = key;    # If we have not reached maxLoop we can then travel back through the stack setting our new index values accordingly
        return (table1, table2);
    else:
        newData = rehash(len(table1));
        table1 = newData[0];
        table2 = newData[1];
    return (table1, table2);



# hashInfo is a class we will make objects with that will contains h1 and h2 for each hashing instance of our data structure
class hashInfo:
    randomVar1 = random.randint(1,1000000); # Temporarily bounding random values 1-1m
    randomVar2 = random.randint(1,1000000);
    def hFunc(self, key, listLength, primeValue):
        hashedAddress = ((self.randomVar1 * key + self.randomVar2) % primeValue) % listLength;
        return(key, hashedAddress);

