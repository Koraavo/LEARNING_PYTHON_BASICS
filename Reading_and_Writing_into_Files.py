import os
def understanding_reading_files():
    """
        # File Objects
        # Open file
        # READING FILES
        # Method 1:
            # when the file is in the same directory
            f = open('Reading_and_Writing_Test_File.txt')

            # if you want to open the file from a different path

            Way1:
                import sys
                sys.path.append('The path where the file exists')

            Way2:
                changing environment variable
                open .bash_profile with texteditor
                nano ~/.bash_profile
                towards the end of the file:
                export PYTHONPATH = 'Enter the location'
                save by pressing crtl+x and Y and enter
                restart terminal



        The modes are:

        ‘r’ – Read mode which is used when the file is only being read
        ‘w’ – Write mode which is used to edit and write new information to the file
        (any existing files with the same name will be erased when this mode is activated)
        ‘a’ – Appending mode, which is used to add new data to the end of the file;
        that is new information is automatically amended to the end
        ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file


        # print name of the file
        print(f0.name)

        # mode of the file
        print(f0.mode)

        # Important to close the file if files are opened this way
        f.close()

        #PREFFERED METHOD
        # Open the file using context manager
        # when you exit the block, the file will automatically close

            file_path = '/Volumes/Kinjal/PYTHON-LEARNING/1 PROJECTS_PYCHARM_SCRIPTS/Python_Files/word_cloud/'
            tale_of_two_cities = 'charles.txt'
            file_path = os.path.join(file_path, tale_of_two_cities)
            print(file_path) # making sure that the path is correct

            with open(file_path, 'r') as charles:
                # Read the whole text in one line
                charles_lines = charles.readlines() # one line for the whole text
                print(charles_lines)

                # read single line everytime this is executed
                single_line_read = charles.readline()
                print(single_line_read, end='')

                # reads the whole content but takes memory space in the computer
                charles_contents = charles.read() # will take memory space

                # What if we want to read a big text file
                # but do not want to load all the contents of the file into memory
                # otherwise we can run out of memory
                # this is efficient because it is not reading all the contents of the file all at once
                Method1:
                    for line in charles:
                        print(line, end='')

                Method2:
                    # Chunk Method
                        # Print the first 1000 characters for a file for example:
                        charles_contents = charles.read(1000)
                        print(charles_contents)

                        # Print the next 1000 characters of the file
                        charles_contents1 = charles.read(1000)
                        print(charles_contents)

                    #using a while loop:
                        with open(file_path, 'r') as charles:
                            size_to_read = 100
                            charles_contents = charles.read(size_to_read)

                        while len(charles_contents) > 0:
                            print(charles_contents, end='')
                            charles_contents = charles.read(size_to_read)

                # What if we wnt to start the reading again from
                #the beginning instead of appending the next 100 characters

                charles_contents = charles.read(size_to_read)
                print(charles_contents, end='')

                charles.seek(0) # can change to any location you want

                charles_contents = charles.read(size_to_read)
                print(charles_contents, end='')

        #WRITING FILES
        # If file exists write will overwrite the file created
        # BEWARE

        with open('test2.txt', 'w') as file:
            file.write('TEST')
            file.write('REST') # will write the text back to back
            file.seek(0) # will overwrite the data(as per the length of the character)
            file.write('CREST')

        # Copying data from one file to another
        with open('Reading_and_Writing_Test_File.txt', 'r') as rf: # readfile
            with open('test2.txt', 'w') as wf:  # writefile
                for line in rf: # for each line in readfile
                    wf.write(line) # write the line as it is in the writefile

        # Copy a picture file
        # need to read pictures in binary mode
        Method1:
            with open('call me by your name.jpg', 'rb') as rf: # readfile
                with open('call me by your name1.jpg', 'wb') as wf:  # writefile
                    for line in rf: # for each line in readfile
                        wf.write(line) # write the line as it is in the writefile

        #Method2:
        # with chunk_size
            with open('call me by your name.jpg', 'rb') as rf:  # readfile
                with open('call me by your name1.jpg', 'wb') as wf:  # writefile
                    chunk_size = 4096
                    rf_chunk = rf.read(chunk_size)
                    while len(rf_chunk)> 0:
                        wf.write(rf_chunk)
                        rf_chunk = rf.read(chunk_size)

        """
    pass

help(understanding_reading_files)