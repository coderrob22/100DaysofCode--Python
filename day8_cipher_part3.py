alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(beginning_text, shift_amount, encode_decode):
  coded_text = ""
  for letter in beginning_text:
    position = alphabet.index(letter)
    if encode_decode == "encode":
      new_position = position + shift_amount
    else:
      new_position = position - shift_amount
    coded_text += alphabet[new_position]
  print(f"The {direction}d text is {coded_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(beginning_text=text, shift_amount=shift, encode_decode=direction)