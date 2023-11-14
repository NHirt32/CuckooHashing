import random
import math

largePrime = 7919;

# rehash is the function that manually doubles the size of our tables and creates new hash functions
def rehash(currSize):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print("WE ARE AT MAXLOOP => REHASHING");
    print(f'Our current size pre doubling: {currSize}');
    currSize = currSize * 2;
    # Manually we are doubling the size of our tables and setting their lengths with 'None' values
    print(f'Our current size post doubling: {currSize}');
    table1 = [None] * currSize;
    table2 = [None] * currSize;
    tableStatePrint(table1, table2);
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    hash1 = hashInfo();
    hash2 = hashInfo();
    return (table1, table2, hash1, hash2);

# hashInsert parameters are our two tables, our key value, the hashed index of our key, and the current number of
# iterations in the current attempted insert
def hashInsert(table1, table2, hash1, hash2, key, loopCount, maxLoop):
    loopCount += 1;
    # The idea of this loop is to attempt insertion in t1, if the index is already taken insert anyways...
    # Then swap the order of t1, t2, h1, h2 and use the value that was already present in t1 and insert it into our new t1 (t2)
    # It will oscillate between t1 and t2 if necessary until it reaches maxLoop
    # If the index of t1 is not taken simply insert and break out of our while loop
    while loopCount <= maxLoop:
        tableStatePrint(table1, table2);
        index = hash1.hFunc(key, len(table1), largePrime);
        print(f'We are inserting {key} at {index}. This is loop {loopCount} where our maxLoop is {maxLoop}');
        if table1[index] is None:   # If our table[index] is None we set table[index] = key
            table1[index] = key;
            break;
        elif table1[index] is not None: # If our table[index] isn't None
            table1[index], key = key, table1[index]; # Sets table1[index] = key, and the next iteration of our key = the original table1[index]
            # Swap positions of table/hash 1s and 2s
            table1, table2 = table2, table1;
            hash1, hash2 = hash2, hash1;
        loopCount += 1;
    if loopCount >= maxLoop:    # If our previous while loop
        table1, table2, hash1, hash2 = rehash(len(table1));
        return (table1, table2, hash1, hash2, False);
    return (table1, table2, hash1, hash2, True);



def cuckooHash():
    # Dummy data for testing
    lowerBound = 1;
    upperBound = 102;
    currSize = 5;  # This is 'r' from the paper
    sampleAmount = 2 * currSize;  # This is r^2 from the paper, temporarily 2r since idk whats happening...
    dataSet = random.sample(range(lowerBound, upperBound), sampleAmount);  # Random sample of keys
    maxLoop = 3 * math.log(len(dataSet), 2);  # Base should be 1 + epsilon, can't access resource tho...
    completed = False; # We will use this variable to determine if we have rehashed in an insertion attempt

    table1 = [None] * currSize;  # From the paper both table1, and table2 are of length 'r'
    table2 = [None] * currSize;

    hash1 = hashInfo();
    hash2 = hashInfo();

    print(f'Our data set: {*dataSet,}')
    while completed == False:
        completed = True;
        for key in dataSet:
            table1, table2, hash1, hash2, completed = hashInsert(table1, table2, hash1, hash2, key, 0, maxLoop); # Note that unless completed = False hash1 and hash2 will not change
            if completed == False:  # If we have rehashed change our hashing functions and restart the process of inserting keys into our new fresh tables
                break;

    tableStatePrint(table1, table2);


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