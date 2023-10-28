alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceaser_incrypt(plaintext, key):
    assert key > 0
    cyphertext = ""
    plaintext = plaintext.lower()
    for letter in plaintext: # hello
        # print(letter)
        cyphertext += alphabet[(alphabet.index(letter) + key) % 25] 
        # print(cyphertext)
    return cyphertext


def ceaser_decrypt(cyphertext, key):
    assert key > 0
    plaintext = ""
    for letter in cyphertext:
        plaintext += alphabet[(alphabet.index(letter) - key) % 25] 
    return plaintext 



print(ceaser_incrypt("Hello", 7))

cyphertext = ceaser_incrypt("hello", 7)

print(ceaser_decrypt(cyphertext, 7))
# print(ceaser_decrypt(cyphertext, 8))
key = 7
print(f"===== Caesar decryption demo =====\nciphertext: {cyphertext}, key: {key}")
print(f"decrypted: {caesar_decrypt(cyphertext, key)}")
