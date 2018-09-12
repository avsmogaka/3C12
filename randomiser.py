#!/usr/bin/env python3
import random, time
post = time.strftime("%c")
def ile():
    """this funtion is created for invocation purposes by another program. Abstraction for newbies.
    uncomment every '#print...' funtion if you intend to see the output in the commandline or your SuperIDLE.
    """
    #print(post)
    #print("  1   2   3   4   5   6   7   8   9   10  11  12")
    #print(" ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___")
    df = open('/home/avstin/prog/craze/py/prminer/dumpfile.txt', "a")
    #df is the file object
    df.write(" *** *** *** *** *** *** *** *** *** *** \n\n            ")
    #df.write is used to write to the dumpfile. /n/n creates a "line spacing of two"
    df.write(post)
    #used to print the date, time a record was made in the dumpfile
    df.write("\n\n  1   2   3   4   5   6   7   8   9   10\n")
    #this will be used to differentiate the outcome number in the randomize algorithm
    df.write(" ___ ___ ___ ___ ___ ___ ___ ___ ___ ___\n")
    #some house keeping for heavens sake, learnt from bobota
    df.close()
    #thwis will be used to close the dumpfile after appending the functions data
def ore():
    for c in range(1,18):
        #this loop sequence runs seventeen time in correspondence to the number of games.
        for b in range(1,11):
            #this loop sequence runs twelve times, should be altered to suit the purpose.
            a = random.randrange(0,3)
            #randomly generate a value from a choice of three values, 0, 1, 2.
            if a == 0:
                #this conditional statement determines what to be printed given a certain outcome.
                #if the random outcome is 0 then "| 1" will be printed to the dumpfile.
                #print ("| 1 ", end='')
                df = open('/home/avstin/prog/craze/py/prminer/dumpfile.txt', "a")
                #open/create a file named dumpfile.txt in the specified directory. Using append mode data is added to the file.
                #note that the write mode will destroy all data before starting to write.
                df.write("| 1 ")
                #outputs "| 1 " if the value cast is 0.
                df.close()
                #open a file, write in the file and close it, also in the other if statements.
            elif a == 1:
                #if the random outcome is 1 then "| X" will be printed to the dumpfile.
                #print ("| X ", end='')
                df = open('/home/avstin/prog/craze/py/prminer/dumpfile.txt','a')
                df.write("| X ")
                #outputs "| X " if the value cast is 1.
                df.close()
            elif a == 2:
                #if the random outcome is 2 then "| 2" will be printed to the dumpfile.
                #print ("| 2 ", end='')
                df = open('/home/avstin/prog/craze/py/prminer/dumpfile.txt', "a")
                df.write("| 2 ")
                #outputs "| 2 " if the value cast is 2.
                df.close()
        #print("|")
        df = open('/home/avstin/prog/craze/py/prminer/dumpfile.txt', "a")
        df.write("|\n")
        #ensures that random data is now printed in a new line inside the dumpfile.
        df.close()
