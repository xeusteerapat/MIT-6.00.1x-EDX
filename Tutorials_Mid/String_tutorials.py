# Index slicing remember how index slicing works as below
# [start: end: step]
# substring [start:stop]
# last index is *** exclusive ***

a = 'I_Love_Coding'
print(a[5:10])  # e_Cod start from 5 to 9 (10 is exclusive)

print(a[2:12:2])  # Lv_oi start from 2 to 10 with step of 2

print(a[10:10:2])  # empty string

print(a[:5])  # I_Lov start from 0 to 5

print(a[11:])  # ng start from 11 to end

print(a[::3])  # Io_dg start from 0 to end step of 3

print(a[2::3])  # Leon start from 2 to end step of 3

print(a[:8:4])  # Iv start from 0 to 8 step of 4
