alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play_again = True
while play_again:
    direction = input("Type encode to encrypt, type decode to decrypt: \n").lower()
    text = input("type in your message: \n").lower()
    shift_number = int(input("enter shift number: \n"))
    replay = input("Do you want to play again? Y or N: ")

    if play_again == "no":
        play_again = False
        print("Game over")
    else:
        play_again = False


def ceaser(plain_text, shift_amount, choice):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if choice == "encode":
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter

            elif choice == "decode":
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter

        else:
            cipher_text += char

    print(f"the {choice} text is {cipher_text}")


shift_number = shift_number % 26

ceaser(plain_text=text, shift_amount=shift_number, choice=direction)


