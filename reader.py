import pyttsx3
import PyPDF2
book = open('t.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
speaker = pyttsx3.init()





print(pages)

page = pdfreader.getPage(10)
text = page.extractText()

speaker.say(text)

speaker.runAndWait()