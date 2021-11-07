# %%

def rotate(string: str):
    return string[1:] + string[0]


# %%
def scramble(scrambler_input: str, scrambler_output: str, scrambler_input_position: int):
    scrambler_letter = scrambler_input[scrambler_input_position]
    return scrambler_output.index(scrambler_letter)


# %%


def cypher_letter(letter: str, scramblers: list, reflector: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet.index(letter)

    for scrambler_input, scrambler_output in scramblers:
        position = scramble(scrambler_input, scrambler_output, position)

    position = scramble(
        alphabet, reflector, position)

    for scrambler_input, scrambler_output in scramblers:
        position = scramble(scrambler_output, scrambler_input, position)

    return alphabet[position]

# %%


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

scrambler_output = "UWYGADFPVZBECKMTHXSLRINQOJ"

reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


assert (cypher_letter(
    "P", [(alphabet, scrambler_output)], reflector) == "G")

# %%


def enigma(input_string: str, scrambler, reflector: str):
    cyphered_string = ""
    for letter in input_string:
        # girar scramblers
        scrambler = (rotate(scrambler[0]), rotate(scrambler[1]))

        # ciphramos letra
        cyphered_letter = cypher_letter(letter, [scrambler], reflector)

        # agregar al resultado
        cyphered_string += cyphered_letter

    return cyphered_string

# %%

assert (enigma(
    "Z", (alphabet, scrambler_output), reflector) == "U")

# %%
assert (enigma(
    "ZYDNI", (alphabet, scrambler_output), reflector) == "ULTRA")
# %%
