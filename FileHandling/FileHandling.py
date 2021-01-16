import os


def main():
    '''
        if the execution context is the root directory and if I want to open a file in that directory itself
        then in that case, I need to directly give the file name instead of the usual ../ or ..\\
        so in the below open(file='../.gitignore') will not work since it will go outside the current directory.

        By default the file is open in read mode which is denoted by 'r'
        For write mode it is 'w' which will essentially clear the existing file and then start writing
        from the beginning of the file
        For append mode it is 'a' which will mean that the cursor will start to write from whereever the
        last line in the file ended

        Additionally a '+' can be used in the 'r' mode to open the file in read & write mode.
        There is additionally a 'b' or 't' which will lead to the file being opened in binary or text mode
        and the default is text mode

        Worth noting about the 'r+' mode is that once a file is read, the additional data written to the file
        will not be read by the loop that runs on the file
    '''
    file = open(file='./FileHandling/filehandling.txt', mode='r+') #open(file='./FileHandling/filehandling.txt', mode='r+')
    file.write('potato')
    """ 
        as a good practice, always close a file once it is written to else one could end up with a corrupt file
    """
    # file.close()
    """ 
        If the flush method is called before reading from the file even once the it writes the data to the first line replacing the existing data
        If the file is read once, it writes to the end of the file, which kind of makes sense considering that reading will take the file
        cursor to the end of whatever line was read

        TODO: Find if the above understanding is true or there's more to it.
    """
    # file.flush()
    for line in file:
        print(line)
        '''
            this will remove all the line endings from the file and/or any additional spaces at the end of line
            meaning that one will not have to worry about any of the new line hidden characters and all of that
        '''
        # print(line.rstrip())
    
    # Reading file in binary mode
    # Below code will print the image as garbage values since the image is a binary data
    binary_mode_file = open('./FileHandling/random.jpg', mode='rb')
    for line in binary_mode_file:
        """
            As a good practice, always have a buffer when reading a binary file as one might not know what would be the
            size of the file to be read
            buffer = line.read(10240) 
        """
        print(line.strip())

if __name__ == "__main__":
    main()