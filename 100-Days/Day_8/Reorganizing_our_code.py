alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode to encrypt, type decode to decrypt: \n").lower()
text = input("type in your message: \n").lower()
shift_number = int(input("enter shift number: \n"))


def ceaser(plain_text, shift_amount, choice):
    cipher_text = ""
    for each_letter in plain_text:
        position = alphabet.index(each_letter)
        if choice == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter

        elif choice == "decode":
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"the {choice} text is {cipher_text}")


ceaser(plain_text=text, shift_amount=shift_number, choice=direction)
