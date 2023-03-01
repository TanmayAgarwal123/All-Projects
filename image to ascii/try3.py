import ascii_magic
output = ascii_magic.from_image_file("Projects/image to ascii/2.jpeg",columns=60)
ascii_magic.to_terminal(output)