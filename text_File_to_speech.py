import os

from gtts import gTTS

fh = open("Goals By Brain Tracy.pdf", "r")
 
myText= fh.read().replace("\n", " ")

language='en'

output=gTTS(text=myText, lang=language, slow=False)

output.save("outputs.mp3")
fh.close()
os.system("start outputs.mp3")
