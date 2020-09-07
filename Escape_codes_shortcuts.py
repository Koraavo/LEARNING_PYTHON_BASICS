s = "e:\\Beginner"
s1 = "e:" "\\" "Beginner"
s2 = s1 + \
    "\\tst.py"

print ("This is a DOS path:", s)
print ("This is a DOS path:", s1)
print ("This is a DOS path:", s2)

s3 = "I contain 'single' quotes"

print (s3)

s6 = "I contain\t\t\tthree\t\t\ttabs" #\t: TABS
s7 = "I contain a\t\v\tvertical tab" # CHECK IT OUT IN TERMINAL
s8 = "I contain a\t\a\tBELL, which you can hear"

print (s6)
print (s7)
print (s8) # returns a beep on the terminal

s9 = "I contain a BACK\bSPACE"
s10 = "I contain a BACKK\bSPACE AND a \nNEWLINE and a \rLINEFEED"
s11 = "I ve got a FORM\fFEED!"
s20 = "NEWLINE and \ra" # anything before the \r gets deleted, it is like the remove function

print (s9)
print (s10)
print (s11)
print (s20)

s12 = "If Python doesn't know what the escape code\n" \
"means, it performs the identity operation!  \identity!"
s13 = "But if you don't know what a code means, don't use it!"

print (s12)
print (s13)

s14 = "stackoverflow\rnine" # this in terminal replaces the stac with Pile. four characters in the beginning
print (s14)

print("stackoverflow\fnine\fgreat") # works great in Terminal again