vowels = ['a','e','i','o','u']
string = "Karan"
vowel_count = 0
consonant_count = 0
for i in range(len(string)):
    if string[i] in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print("Vowel Count: ",vowel_count)
print("Consonant Count: ",consonant_count)