# %%

def rotate(string: str, rotations=1):
    return string[rotations:] + string[:rotations]


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

    for scrambler_input, scrambler_output in scramblers[::-1]:
        position = scramble(scrambler_output, scrambler_input, position)

    return alphabet[position]

# %%


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

scrambler_1 = "UWYGADFPVZBECKMTHXSLRINQOJ"

scrambler_2 = "AJPCZWRLFBDKOTYUQGENHXMIVS"

scrambler_3 = "TAGBPCSDQEUFVNZHYIXJWLRKOM"

reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

for scrambler in [scrambler_1, scrambler_2, scrambler_3]:
    assert(len(scrambler) == len(set(scrambler)))

assert (cypher_letter(
    "P", [(alphabet, scrambler_1)], reflector) == "G")

# %%


def enigma(input_string: str, scramblers: list, reflector: str):
    cyphered_string = ""
    for letter in input_string:
        # girar scramblers
        # TODO: girar el resto de los scramblers para mensajes mayores a 26 letras
        scramblers[0] = (rotate(scramblers[0][0]), rotate(scramblers[0][1]))

        # ciphramos letra
        cyphered_letter = cypher_letter(letter, scramblers, reflector)

        # agregar al resultado
        cyphered_string += cyphered_letter

    return cyphered_string

# %%


assert (enigma(
    "Z", [(alphabet, scrambler_1)], reflector) == "U")

# %%
assert (enigma(
    "ZYDNI", [(alphabet, scrambler_1)], reflector) == "ULTRA")
# %%

#PURPLE#
enigma(
    "QHSGUWIG", [(rotate(alphabet, 4), rotate(scrambler_1, 4))], reflector)
# %%
assert(
    enigma(
        "QHSGUWIG",
        [
            (rotate(alphabet, 4), rotate(scrambler_1, 4)),
            (alphabet, alphabet),
            (alphabet, alphabet)
        ], reflector)
    ==
    "XVPURPLE"
)

# %%

enigma("HUGRVFQRXU", [(alphabet, scrambler_2),
                      (rotate(alphabet, 4), rotate(scrambler_1, 4)),
                      (rotate(alphabet), rotate(scrambler_3))], reflector
       )
# %%
rotate(alphabet)

# %%

# %%
word = "GYHRVFLRXY"
letter = ""

for index, letter in enumerate(word):
    index += 1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_2 = "BACDNFHGIJKQMEOPLRZTYVWXUS"
    position = alphabet_2.index(letter)

    position = scramble(rotate(alphabet, index), rotate(scrambler_2, index), position)
    position = scramble(rotate(alphabet, 4 + index // 26), rotate(scrambler_1,  4 + index // 26), position)
    position = scramble(rotate(alphabet), rotate(scrambler_3), position)

    position = scramble(
        alphabet, reflector, position)

    position = scramble(rotate(scrambler_3), rotate(alphabet), position)
    position = scramble(rotate(scrambler_1, 4), rotate(alphabet, 4), position)
    position = scramble( rotate(scrambler_2, index), rotate(alphabet, index),position)


    print(alphabet_2[position])
# %%


alphabet =    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
scrambler_2 = "AJPCZWRLFBDKOTYUQGENHXMIVS"
scrambler_1 = "UWYGADFPVZBECKMTHXSLRINQOJ"
scrambler_3 = "TAGBPCSDQEUFVNZHYIXJWLRKOM"
reflector =   "YRUHQSLDPXNGOKMIEBFZCWVJAT"

HUGRVFQRXU

"H"

"BACDNFHGIJKQMEOPLRZTYVWXUS"

"BCDEFGHIJKLMNOPQRSTUVWXYZA"
"JPCZWRLFBDKOTYUQGENHXMIVSA"

"EFGHIJKLMNOPQRSTUVWXYZABCD"
"ADFPVZBECKMTHXSLRINQOJUWYG"

"BCDEFGHIJKLMNOPQRSTUVWXYZA"
"AGBPCSDQEUFVNZHYIXJWLRKOMT"

"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"YRUHQSLDPXNGOKMIEBFZCWVJAT"