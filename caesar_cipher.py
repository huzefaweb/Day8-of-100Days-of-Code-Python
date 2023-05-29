# ---------------- CAESAR CIPHER ------------------ my way
# alphabet = [
#   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
#   'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#   't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
# yes = True

# while yes:
#   direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   if direction == "encode":

#     def encrypt(plain_text, shift_amount):
#       cipher_text = ""
#       for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#       print(f"The encrypt text is {cipher_text}")

#     encrypt(plain_text=text, shift_amount=shift)
#   else:

#     def decrypt(plain_text, shift_amount):
#       cipher_text = ""
#       for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#       print(f"The decrypt text is {cipher_text}")

#     decrypt(plain_text=text, shift_amount=shift)
#   ask = input("Do you want to this again: Type 'yes' or 'no':\n").lower()
#   if ask == "no":
#     yes = False

# ------------- course way ----------------
from art import logo

print(logo)
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      end_text += new_letter
    else:
      end_text += char
  print(f"Here's the {direction}d result: {end_text}")


while_continue = True
while while_continue:
  direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input(
    "Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
  if result == "no":
    while_continue = False
    print("Good Bye")
