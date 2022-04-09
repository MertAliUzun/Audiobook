import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
def openBook(choice):
  if choice == "1":
    book = open('Kafka.pdf', 'rb')
  elif choice == "2":
    book = open('lof.pdf', 'rb')
  elif choice == "3":
    book = open('bnw.pdf', 'rb')
  elif choice == "4":
    book = open('anifarm.pdf', 'rb')
  elif choice == "5":
    book = open('cworange.pdf', 'rb')
  else:
      book = open('Kafka.pdf', 'rb')
      print("Invalid Entry")
      exit()
  return book
choice = input("1.Metamorphosis\n" + "2.Lord of Flies \n" + "3.Brave New World \n" +
               "4.Animal Farm \n" + "5.A Clockwork Orange \n" + "Please Select the Book: ")
book = openBook(choice)
pdfReader = PyPDF2.PdfFileReader(book, strict=False)
maxPage = pdfReader.numPages - 1
i = 0
while i <= maxPage:
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    print(text)
    speaker.runAndWait()
    i += 1
