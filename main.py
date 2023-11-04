
# rehash is the function that manually doubles the size of our tables
def rehash(currSize, table1, table2):
    currSize = currSize * 2;
    # Manually we are doubling the size of our tables and setting their lengths with 'None' values
    table1 = [None] * currSize
    table2 = [None] * currSize
    return (table1,table2, currSize);

# hashify is a function that applies our universal hash functions to keys, returns (key,index) tuple
def hashify(key):
    hashedIndex = hash(key) % currSize;    # Temporarily using hash() instead of univ hash
    return (key, hashedIndex)


# Dummy data for testing
table1 = [0,1,2,3];
table2 = [4,5,6,7];
keys = [*range(1,101,1)];   # In this example r^2=100
currSize = len(keys);

# Testing rehash
newData = rehash(currSize, table1, table2);
# Setting new values post rehash
table1 = newData[0];
table2 = newData[1];
currSize = newData[2];
testHash = hashify(keys[1]);


# Practice printing
# print(table1);
# print(table2);
# print(currSize);
# print(testHash[1]);
print(hash(keys));