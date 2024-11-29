def vowel_count(word):
    vowels="aeiou"
    count=0
    for char in word:
        if char in vowels:
            count=count+1
            print(char,end=" ")
    print()
    return count
name=(input("enter name: ".lower()))
vowel_all=vowel_count(name)
print(f"total vowel in {name} is {vowel_all}")