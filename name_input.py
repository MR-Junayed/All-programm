def vowel_count(text):
    vowel="aeiouAEIOU"
    consonent = "zxcvbnmlkjhgfdspytrwqZXCVBNMLKJHGFDSPYTRWQ"
    count=0
    for i in text:
        if i in vowel:
            count = count + 1
            print(i,end=" ")
    return count
def cons_count(text):
    cons = "zxcvbnmlkjhgfdspytrwqZXCVBNMLKJHGFDSPYTRWQ"
    count=0
    for i in text:
        if i in cons:
            count = count + 1
            print(i, end=" ")
    return count
name=input("Enter Name: ")
v=vowel_count(name)
c=cons_count(name)
print("\n",v,c)