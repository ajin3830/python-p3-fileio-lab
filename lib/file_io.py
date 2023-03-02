import ipdb
def write_file(file_name, file_content):
    # WHY INTERPOLATION??
    # To make it dynamic-> when you pass in file_name, you're accessing
    # the value of file_name, not file_name itself, unless the name of 
    # file is file_name
    with open(f'{file_name}.txt', 'w') as file_name:
        file_name.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode = 'a') as file_name:
        file_name.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as file_name:
        # return it so you can read, no need to return when writing bc
        # you already know what you're writing
        return file_name.read()
    
# You should use `with open()` statement when working with files in Python 
# bc it provides a clean & safe way to open and manipulate files in your code 


# # open a file, only 1 required arg is the path to file
# text_file = open('file_directory/file_name.tx')
# # default mode when open a file is read, or print it to find out
# print(text_file.mode)
# # but can specify mode such as encoding attribute
# text_file = open('file_directory/file_name.txt', encoding='utf-8')
# # append mode
# text_file = open('file_directory/file_name.txt', mode='a', encoding='utf-8')

# # close a file
# text_file.close()
# # close a file automatically using with
# with open('file_name.txt', encoding='urf-8') as text_file:
#     text_file.read()

# # read a file using .read() method
# print(text_file.read())
# # read 1 line at a time
# with open('big_file.txt', encoding='utf-8') as text_file:
#     for line in text_file:
#         # Process the individual line
#         print(line)

# # write to a file using .write() method
# # mode='w'overwrites the file
# with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
#     log_file.write('Log 1')
# # mode='a' append to existing file
# with open('log_file.txt', mode='a', encoding='utf-8') as log_file:
#     log_file.write('Log 2')