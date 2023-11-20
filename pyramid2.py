#3
a='amity'
for i in range(len(a)-4):
    print(a[0])
    print(a[i-i+1:2]*2)
    print(a[i-i+2:3]*3)
    print(a[i-i+3:4]*4)
    print(a[i-i+4:5]*5)
    print(a[-2]*4)
    print(a[-3]*3)
    print(a[-4]*2)
    print(a[-5])
