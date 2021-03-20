import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#print(data)
#Loop through rows of a data frame
# for (index, row) in data.iterrows():
#     print(nato_dict)

    #Access index and row

    #Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phoenetic():

    user_input = input("Enter Word: ").upper()
    # Loop through each letter and find matching key and add the value to the word list
    #for letter in user_input:
    try:
        output_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters of the alphabet")
        generate_phoenetic()
    else:
        print(output_list)
generate_phoenetic()