: str) -> str:
    rot7, rot9 = 7, 9  # Rotation values
    vowels = 'AEIOUaeiou'  # Vowels to check
    decrypted = []  # List to hold decrypted characters

    for index, char in enumerate(password):
        if char in vowels:
            rotation_key = rot9 if index % 2 == 1 else rot7  # Use 9 for odd indices
            decrypted.append('0')  # Add '0' before the vowel
        else:
            rotation_key = rot7 if index % 2 == 0 else rot9  # Use 7 for even indices

        if 33 <= ord(char) <= 126:  # Check if character is within the allowed ASCII range
            decrypted_char = chr((ord(char) - rotation_key - 33) % 94 + 33)  # Wrap around
            decrypted.append(decrypted_char)  # Add decrypted character to the list
        else:
            decrypted.append(char)  # Append unchanged if out of range

        if char in vowels:
            decrypted.append('0')  # Add '0' after the vowel

    return ''.join(decrypted)  # Join the list into a string and return

# Test case
print(decrypt_password("bAnanASplit"))  # Expected: "i0J0u0j0u0J0Zys0r0{"

Expected Output:
When I run decrypt_password("bAnanASplit"), I expect the output to be "i0J0u0j0u0J0Zys0r0{".
Actual Output:
Instead, I get "0b0'C'0n0'c'0n0'C'Spl'k't".


Debugging Efforts:
I've tried adding print statements to track the character transformations, but I'm still getting incorrect results.
Environment:
I'm using Python 3.12.
Any help on what might be going wrong would be greatly appreciated!
