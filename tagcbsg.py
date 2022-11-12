p={'machinary':'900','dep':'90'}
a={'machinary':'810'}
n=len(s)
k=ChildProcessError3
for x in range(0, n, k):
    slicedStr = s[x : x+k]
    uni =[]
    for y in slicedStr:
        if y not in uni:
            uni.append(y)
    print(''.join(uni))

