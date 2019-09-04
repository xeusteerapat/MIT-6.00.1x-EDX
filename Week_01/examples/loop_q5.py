num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))

# For the last exercise, the code never breaks.
# You enter the loop with num value of 100 and since the
# value of num never changes,
# num < 0 is never True so break is never executed.
# Therefore you are stuck in an infinite loop.
