import random
import math

largePrime = 7919;

# rehash is the function that manually doubles the size of our tables
def rehash(currSize):
    currSize = currSize * 2;
    # Manually we are doubling the size of our tables and setting their lengths with 'None' values
    table1 = [None] * currSize
    table2 = [None] * currSize
    hash1 = hashInfo();
    hash2 = hashInfo();
    return (table1, table2, hash1, hash2);

# hashInsert parameters are our two tables, our key value, the hashed index of our key, and the current number of
# iterations in the current attempted insert
def hashInsert(table1, table2, hash1, hash2, key, loopCount, maxLoop):
    loopCount += 1;
    tableStatePrint(table1, table2);
    index = hash1.hFunc(key, len(table1), largePrime);
    if(maxLoop > loopCount):   # If we haven't reached the maximum number of attempted inserts...
        print(f'Insertion Info: Table1 Index = {index}, Key Value = {key}, Current Loop = {loopCount}, maxLoop = {maxLoop}');
        if table1[index] is None:    # If the index is empty from a rehash or from initial creation we can simply insert the value
            table1[index] = key;    # Set the value of the index = to our key
        else:
            hashInsert(table2, table1, hash2, hash1, table1[index], loopCount, maxLoop);  # If the index isn't empty we recursively call hashInsert again swapping the table we are inserting to as well as the value we are trying to insert
            table1[index] = key;    # If we have not reached maxLoop we can then travel back through the stack setting our new index values accordingly
        return (table1, table2);
    else:   # If we have reached the maximum number of attempted inserts...
        print("MAX LOOP HAS BEEN REACHED REHASHING")
        newData = rehash(len(table1));
        table1 = newData[0];
        table2 = newData[1];
        hash1 = newData[2];
        hash2 = newData[3];
    return (table1, table2);

def cuckooHash():
    # Dummy data for testing
    lowerBound = 1;
    upperBound = 102;
    currSize = 10;  # This is 'r' from the paper
    sampleAmount = 2 * currSize;  # This is r^2 from the paper, temporarily 2r since idk whats happening...
    dataSet = random.sample(range(lowerBound, upperBound), sampleAmount);  # Random sample of keys
    maxLoop = 3 * math.log(len(dataSet), 2);  # Base should be 1 + epsilon, can't access resource tho...

    table1 = [None] * currSize;  # From the paper both table1, and table2 are of length 'r'
    table2 = [None] * currSize;

    hash1 = hashInfo();
    hash2 = hashInfo();

    print(f'Our data set: {*dataSet,}')

    for key in dataSet:
        newValues = hashInsert(table1, table2, hash1, hash2, key, 0, maxLoop);
        table1 = newValues[0];
        table2 = newValues[1];



# hashInfo is a class we will make objects with that will contains h1 and h2 for each hashing instance of our data structure
class hashInfo:
    randomVar1 = random.randint(1,1000000); # Temporarily bounding random values 1-1m
    randomVar2 = random.randint(1,1000000);
    def hFunc(self, key, listLength, primeValue):
        # print(f'key = {key}, listLength = {listLength}');
        hashedAddress = ((self.randomVar1 * key + self.randomVar2) % primeValue) % listLength;
        return hashedAddress;


# Debug printing
def tableStatePrint(table1, table2):
    print("---------------------------------------")    # Formatting
    print(f'Table 1: {*table1,}');
    print(f'Table 2: {*table2,}')