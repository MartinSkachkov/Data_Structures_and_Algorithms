def count_characters(s):
    # Initialize an empty dictionary
    char_count = {}

    # Iterate over each character in the string
    for char in s:
        if char in char_count:
            # Increment the count if the character is already in the dictionary
            char_count[char] += 1
        else:
            # Add the character to the dictionary with count 1
            char_count[char] = 1

    return char_count

def are_anagrams(str1, str2):
    # Count the frequency of characters in both strings
    count1 = count_characters(str1)
    count2 = count_characters(str2)

    # Compare the dictionaries
    return count1 == count2

print(are_anagrams("restful","fluster"))