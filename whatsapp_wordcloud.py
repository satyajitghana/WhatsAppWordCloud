import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

def sanitize_messages(file,
                      remove_common_words = False,
                      unwanted_words = ["arre", "Arre", "Aur", " aur ", " mai ", " Mai ",
                                        " raha ", " Raha ",
                                        " bhi ", "nahin", "nhi", " haan ", "haan"
                                        "Haan", " ka ", " kuch ", " toh ",
                                        " hee ", "kya", "Kya", "The",
                                        " a ", " and ", " or ", " I ", " i ",
                                        " am ", " Am ", " are ", " Hai ", " hai "],
                      unwanted_words_in_sentences = ["magnet",
                                                     "file attached",
                                                     "https://",
                                                     "http://",
                                                     "This message was deleted",
                                                     "Media omitted",
                                                     "Tap for more info",
                                                     "You deleted this message",
                                                     "that you are trying to send a payment"]):
    texts = file.read()
    sanitized_input = []
    for line in texts.split("\n"):
        actual_text = re.sub('^(.*:)',"", line).strip()
        if (not any(s in line for s in unwanted_words_in_sentences)) and (actual_text is not ""):
                if remove_common_words:
                    for word in unwanted_words:
                        actual_text = actual_text.replace(word, " ")
                sanitized_input.append(actual_text)

    return '\n'.join(sanitized_input)

def create_word_cloud(args):
    texts_file = args.textfile
    file = open(texts_file, mode='r', encoding='utf-8')
    texts = sanitize_messages(file, args.r)
    if args.maskfile is not None:
        mask = np.array(Image.open(args.maskfile))
        wc = WordCloud(scale=4, background_color="white", margin=args.margin, max_words=(texts.count(' ') + texts.count('\n')), mask=mask)
        wc.generate(texts)
        image_colors = ImageColorGenerator(mask)
        wc.recolor(color_func=image_colors)
    else :
        wc = WordCloud(width=800, height=400, scale=3, margin=args.margin, max_words=(texts.count(' ') + texts.count('\n')),
                       background_color='white').generate(texts)
    wc.to_file(args.outputfile+".png")
    file.close()
