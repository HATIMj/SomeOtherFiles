def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        line=string[i:i+k]
        seen=''
        for i in line:
            if i not in seen:
                seen+=i
        print(seen)
        

        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)