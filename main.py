import math
import random

import hashing

# Dummy data for testing
lowerBound = 1;
upperBound = 100;
sampleAmount = 5;
dataSet = random.sample(range(lowerBound,upperBound), sampleAmount); # From the paper we should have r^2 keys
currSize = 10;
maxLoop = 3 * math.log(len(dataSet), base); # Base should be 1 + epsilon, can't access resource tho...

table1 = [0];   # From the paper both table1, and table2 are of length 'r'
table2 = [0];

# Testing rehash
newData = hashing.rehash(currSize);
# Setting new values post rehash
table1 = newData[0];
table2 = newData[1];

print(f'Table Data post rehash(): \nLength of tables: {currSize}');

table1Hash = hashing.hashInfo();

hashVal = table1Hash.hFunc(dataSet[0], len(table1), 859);
print(hashVal);

# Before trying hashInsert
loopCount = 0;

# Practice printing
# print(table1);
# print(table2);
# print(currSize);
# print(testHash[1]);
