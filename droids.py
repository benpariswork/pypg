import sys
import cowsay

droids = r'''
\
 \
 
                                     /~\
                                    |oo )
                                    _\=/_
                    ___            /  _  \
                   /() \          //|/.\|\\
                 _|_____|_        \\ \_/  ||
                | | === | |        \|\ /| ||
                |_|  O  |_|        # _ _/ #
                 ||  O  ||          | | |
                 ||__*__||          | | |
                |~ \___/ ~|         []|[]
                /=\ /=\ /=\         | | |
________________[_]_[_]_[_]________/_]_[_\_________________________
'''

def droid_talk(words):
    cowsay.draw(words, droids)

if __name__ == "__main__":
    try:
        # Attempt to access sys.argv[1]
        argument = sys.argv[1]
        # print(f"The argument provided is: {argument}")
    except IndexError:
        print("Error: You must provide exactly one command-line argument.")
        print("Usage: python my_script.py <your_argument>")
        sys.exit(1)

    droid_talk(argument)
