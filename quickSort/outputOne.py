# case when input is [1, 53, 9, 3, 8, 36, 7, 4]


# the method in the lecture, result of 'quickSortImp()'
'''
inList: [1, 53, 9, 3, 8, 36, 7, 4]
Pivot sub:0 with value:1
final list[1, 53, 9, 3, 8, 36, 7, 4] and comparison 7
partition: [] and [53, 9, 3, 8, 36, 7, 4]

inList: [53, 9, 3, 8, 36, 7, 4]
Pivot sub:0 with value:53
final list[4, 9, 3, 8, 36, 7, 53] and comparison 13
partition: [4, 9, 3, 8, 36, 7] and []

inList: [4, 9, 3, 8, 36, 7]
Pivot sub:0 with value:4
final list[3, 4, 9, 8, 36, 7] and comparison 18
partition: [3] and [9, 8, 36, 7]

inList: [3]
Pivot sub:0 with value:3
final list[3] and comparison 18
partition: [] and []

inList: [9, 8, 36, 7]
Pivot sub:0 with value:9
final list[7, 8, 9, 36] and comparison 21
partition: [7, 8] and [36]

inList: [7, 8]
Pivot sub:0 with value:7
final list[7, 8] and comparison 22
partition: [] and [8]

inList: [8]
Pivot sub:0 with value:8
final list[8] and comparison 22
partition: [] and []

inList: [36]
Pivot sub:0 with value:36
final list[36] and comparison 22
partition: [] and []

[1, 3, 4, 7, 8, 9, 36, 53] 22
'''


# my personal method, result of 'quickSortOri()'
'''
inList: [1, 53, 9, 3, 8, 36, 7, 4]
Pivot sub:0 with value:1
final list[1, 53, 9, 3, 8, 36, 7, 4] and comparison 7
partition: [] and [53, 9, 3, 8, 36, 7, 4]

inList: [53, 9, 3, 8, 36, 7, 4]
Pivot sub:0 with value:53
final list[9, 3, 8, 36, 7, 4, 53] and comparison 13
partition: [9, 3, 8, 36, 7, 4] and []

inList: [9, 3, 8, 36, 7, 4]
Pivot sub:0 with value:9
final list[3, 8, 7, 4, 9, 36] and comparison 18
partition: [3, 8, 7, 4] and [36]

inList: [3, 8, 7, 4]
Pivot sub:0 with value:3
final list[3, 8, 7, 4] and comparison 21
partition: [] and [8, 7, 4]

inList: [8, 7, 4]
Pivot sub:0 with value:8
final list[7, 4, 8] and comparison 23
partition: [7, 4] and []

inList: [7, 4]
Pivot sub:0 with value:7
final list[4, 7] and comparison 24
partition: [4] and []

inList: [4]
Pivot sub:0 with value:4
final list[4] and comparison 24
partition: [] and []

inList: [36]
Pivot sub:0 with value:36
final list[36] and comparison 24
partition: [] and []

[1, 3, 4, 7, 8, 9, 36, 53] 24
'''

