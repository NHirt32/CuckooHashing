import random

import hashing

# Dummy data for testing
lowerBound = 1;
upperBound = 100;
sampleAmount = 5;
dataSet = random.sample(range(lowerBound,upperBound), sampleAmount);
currSize = 10;


table1 = [0];
table2 = [0];

# Testing rehash
newData = hashing.rehash(currSize, table1, table2);
# Setting new values post rehash
table1 = newData[0];
table2 = newData[1];
currSize = newData[2];
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
