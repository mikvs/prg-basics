plain_text = 'The early bird catches the worm'
encrypted_text = ''
for char in plain_text:
    char_code = ord(char)
    char_code += 1
    new_char = chr(char_code)
    encrypted_text += new_char
print(f'Plain text: {plain_text}')
print(f'Encrypted text: {encrypted_text}')