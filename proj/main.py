# Convert text to octal



def text_to_octal(text):
    octal = ""
    for char in text:
        octal += oct(ord(char))[2:].zfill(3)
    return octal

# Convert octal to text
def octal_to_text(octal):
    text = ""
    for i in range(0, len(octal), 3):
        octal_digit = octal[i:i+3]
        text += chr(int(octal_digit, 8))
    return text
