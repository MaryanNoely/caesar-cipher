alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(plain_text, shift_amount):
    '''Function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  shift each letter of the 'text' *forwards* in the alphabet by the shift amount and print the decrypted text.  
  e.g. 
  plain_text = "hello"
  shift = 5
  cipher_text = "mjqqt"
  print output: "The encoded text is mjqqt"'''
  encode_text = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      encode_text += alphabet[new_position]
    else:
      encode_text += letter
  print(f"The encoded text is {encode_text}")


def decrypt(plain_text, shift_amount):  
  '''Function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  e.g. 
  cipher_text = "mjqqt"
  shift = 5
  plain_text = "hello"
  print output: "The decoded text is hello"'''
  
  decode_text = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = int(len(alphabet)/2) + position - shift_amount
      decode_text += alphabet[new_position]
    else: 
      decode_text += letter
  print(f"The decoded text is {decode_text}")


def caesar(direction_selected, plain_text, shift_amount):
  '''Function that encodes or decodes the message based on user inputs'''
  new_text = ""
  if direction_selected == "decode":
    shift_amount=shift_amount*(-1)
  for letter in plain_text:
    if letter in alphabet:      
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if new_position>=len(alphabet):
        new_text+=alphabet[new_position-len(alphabet)]
      else:
        new_text+=alphabet[new_position]
    else:
      new_text += letter

  print(f"The {direction_selected}d text is {new_text}")
  


#Main program that recurrencly encodes or decodes messages based on users inputs

end_of_program=False
action = ["encode", "decode"]
while(end_of_program==False):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  while direction not in action:
    direction = input("Wrong option, type again:\n").lower()
  
  text = input("Type your message:\n").lower()

  shift = int(input("Type the shift number:\n"))
  if shift>=len(alphabet):
    shift%=len(alphabet)

  caesar(direction, text, shift)

  continue_program = input("Do you want to continue encoding/decoding? (Y\\N)\n").lower()
  if continue_program == "n":
    end_of_program = True
