def diff(parm1, parm2):
  diff1 = parm1 - parm2
  arg1 = 20
  diff2 = arg1 - arg2
  print(diff1, diff2)
arg1 = int(input('Enter an integer >'))
arg2 = int(input('Enter an integer >'))
diff(arg1, arg2)
print(arg1, arg2)

def diff(parm1, parm2):
  diff1 = parm1 - parm2
  parm1 = 20
  diff2 = arg1 - arg2
  print(diff1, diff2)
arg1 = int(input('Enter an integer >'))
arg2 = int(input('Enter an integer >'))
diff(arg1, arg2)
print(arg1, arg2)

def diff(parm1, parm2):
  diff1 = parm1 - parm2
  parm1 = 20
  diff2 = parm2 - parm1
  print(diff1, diff2)
parm1 = int(input('Enter an integer >'))
parm2 = int(input('Enter an integer >'))
diff(parm2, parm1)
print(parm1, parm2)

# More Examples
def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = cadabra + word1
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(word1, word2)
main()

# output would be redblue|redblueblue|red blue

def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = cadabra + word1
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  confusion(word2, word2)
main()

# redblue|redblueblue|blueblue