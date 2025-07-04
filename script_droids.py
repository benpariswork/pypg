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
    
    if len(sys.argv) == 2:
        droid_talk(sys.argv[1])
    else:
        print("Usage: python droids.py <argument>")
