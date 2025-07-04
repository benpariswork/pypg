import sys
from ascii_magic import AsciiArt, from_image


if __name__ == "__main__": 
    if len(sys.argv) == 2:
        # This:
        # my_art = AsciiArt.from_image('lion.jpg')
        # my_art.to_terminal()

        # Does the same as this:
        my_art = from_image(sys.argv[1])
        my_art.to_terminal()

    else:
        print("Usage: python droids.py <argument>")
