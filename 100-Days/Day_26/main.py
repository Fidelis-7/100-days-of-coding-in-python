# students_score = {
#     "Alex": 89,
#     "Beth": 90
# }

# sentence = "what is the Airspeed velocity of an unladen swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)
# student_dict = {
#     "student":["Angela", "James","Lily"],
#     "score": [56, 76, 98]
# }
# # for (key,value) in student_dict.items():
# #     print(key)
# import pandas
# student_dataframe = pandas.DataFrame(student_dict)
# # print(student_dataframe)
# for (index, row) in student_dataframe.iterrows():
#     print(row)


import pandas

data = pandas.read_csv("Day_26/nato_phonetic_alphabet.csv")
# print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("only alphabets required")
        generate_phonetics()
    else:
        print(output_list)

generate_phonetics()