def most_frequent(s):
    s = s.lower()
    
    # Initializing the frequency of each letter
    frequency = {}
    
    # Count the frequency of each letter in the string
    for char in s:
        if char.isalpha():  
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    # Sort the dictionary by frequency in decreasing order and alphabetically
    sorted_frequency = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))

    # Print the sorted letters with their frequencies
    for char, count in sorted_frequency:
        print(f"{char} = {count:02}")

# Example usage
input_string = input("Please enter a string: ")
most_frequent(input_string)
