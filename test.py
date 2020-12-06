from pyftools import file
from pyftools import text

def walk_func(path, arg):
    print("path name:", path)

if __name__ == "__main__":
    # walk files
    file_path = "."
    file.walk_files(file_path, walk_func, None)
    xfile = file.load_files(file_path)
    print(xfile)
    print(text.remove_website("https://gitee.com abc"))
    print(text.get_text_charset("test.py"))
    s = text.convert_list2str([123, 456, 'abcdef'], '\n')
    print(s)
    l = text.convert_str2list(s, '\n')
    print(l)
    print(file.get_filename("asdasd/asdas//asdasd/pyftools"))