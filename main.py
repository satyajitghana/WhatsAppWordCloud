import sys, argparse
import numpy as np
from whatsapp_wordcloud import create_word_cloud

def make_parser():
    description = 'A Simple WhatsApp DM Chat WordCloud maker'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--textfile', type=str,
                        default='-', required=True,
                        help='The Whatsapp Chat input file in .txt format')
    parser.add_argument("--maskfile", type=str,
                        help='The Masking image file')
    parser.add_argument("-r", action='store_true',
                        help='Removes the commonly used words')
    parser.add_argument("--margin", type=int,
                        default=2,
                        help='Margin between the words')
    parser.add_argument('--outputfile', type=str,
                        nargs='?',
                        default='output.png',
                        help='file the completed PNG image should be written to' 
                             ' (default: output.png)')

    return parser

def parse_args(arguments):
    parser = make_parser()
    args = parser.parse_args(arguments)
    return args

def main():
    """
    The main entry point
    """
    create_word_cloud(parse_args(sys.argv[1:]))


if __name__ == "__main__":
    main()