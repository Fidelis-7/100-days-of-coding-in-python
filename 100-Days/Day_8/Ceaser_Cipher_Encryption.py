alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode to encrypt, type decode to decrypt: \n").lower()
text = input("type in your message: \n").lower()
shift_number = int(input("enter shift number: \n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for each_letter in plain_text:
        position = alphabet.index(each_letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")


def decrypt(plain_text, shift_amount):
    decoded_text = ""
    for each_letter in plain_text:
        position = alphabet.index(each_letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"the decoded text is {decoded_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift_number)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift_number)
else:
    print("invalid input")