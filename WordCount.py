#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCunt = 0 
  wordCunt = 0
  letterCunt = 0
  for line in textFile:
    lineCunt += 1
    words = line.split()
    print(words)

    for word in words:
      wordCunt += 1
      print(word)


      for letter in word:
        letterCunt += 1
        print(letter)

  print("Lines:", lineCunt)
  print("lines;", wordCunt)
  print("lines:",  letterCunt)

if __name__ == '__main__':
  main()
