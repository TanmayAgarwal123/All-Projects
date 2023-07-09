import ascii_magic
output = ascii_magic.from_image_file("ASCII_image/t.jpg",columns=61)
ascii_magic.to_terminal(output)