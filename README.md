# WhatsAppWordCloud

This makes a word cloud out of your whatsapp conversations, uses the WordCloud Library which does most of the work

SAMPLE USAGE:
``python main.py -textfile WhatsAppChat.txt --maskfile YOUR_MASK.jpg --outputfile "output" --margin 1 -r``

```
usage: main.py [-h] --textfile TEXTFILE [--maskfile MASKFILE] [-r]
               [--margin MARGIN] [--outputfile [OUTPUTFILE]]

A Simple WhatsApp DM Chat WordCloud maker

optional arguments:
  -h, --help            show this help message and exit
  --textfile TEXTFILE   The Whatsapp Chat input file in .txt format
  --maskfile MASKFILE   The Masking image file
  -r                    Removes the commonly used words
  --margin MARGIN       Margin between the words
  --outputfile [OUTPUTFILE]
                        file the completed PNG image should be written to
                        (default: output.png)
```

SAMPLE OUTPUT
![Whatsapp Word Cloud Output](output.png?raw=true "WhatsApp Word Cloud Maker")