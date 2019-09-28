for i in range(3):
    print('----> Outer Loop:', i)
    for j in range(2):
        print('----> Inner Loop:', j)
    print('Out of inner loop, back to outer loop')

"""
----> Outer Loop: 0
----> Inner Loop: 0
----> Inner Loop: 1
Out of inner loop, back to outer loop
----> Outer Loop: 1
----> Inner Loop: 0
----> Inner Loop: 1
Out of inner loop, back to outer loop
----> Outer Loop: 2
----> Inner Loop: 0
----> Inner Loop: 1
Out of inner loop, back to outer loop
"""
