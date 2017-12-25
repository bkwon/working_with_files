"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import itertools
import os.path
# import filecmp

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    if len(line2) > len(line1):
        line1, line2 = line2, line1

    for letter in range(len(line1)):
        try:
            if line1[letter] != line2[letter]:
                return letter

        except IndexError:
            # print("Lines differ at catch position {}".format(letter))
            return letter

    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    special_chars_check = ["\n", "\r"]

    print(len(line1))
    if len(line2) < len(line1):
        shortline = len(line2)
    elif len(line1) < len(line2):
        shortline = len(line1)
    else:
        shortline = len(line1)
    print(range(shortline))

    for specval in special_chars_check:
        try:
            # if c in line1 or c in line2:
            if any(specval in line1 or specval in line2 for specval in special_chars_check):
                print("Detected special chars!")
                return ""
            elif (idx != -1) and idx <= shortline:
                print("Index = " + str(idx) + "; Line1 len = " + str(shortline))
                sep = ('=' * idx)
                seplist = list(sep)
                seplist.append('^')
                sepfinal = "".join(seplist)

                full_string = line1 + "\n" + sepfinal + "\n" + line2 + "\n"
                print(full_string)
                return full_string
            elif (idx == 0) and idx == shortline:
                sep = []
                sep.append('^')
                sepfinal = "".join(sep)
                full_string = line1 + "\n" + sepfinal + "\n" + line2 + "\n"
                print(full_string)
                return full_string
            print("Let's return empty string here.")
            return ""

        except IndexError:
            print("Got an index error here!")
            return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    for lineidx, line1 in enumerate(itertools.zip_longest(lines1, lines2)):
        try:
            line1 = lines1[lineidx]
            line2 = lines2[lineidx]
            index = singleline_diff(line1, line2)
            if index != -1:
                print("Got here!")
                print(lineidx, index)
                return (lineidx, index)

        except IndexError:
            print("Got index error!! --> (" + str(lineidx) + ", 0)")
            return (lineidx, 0)

    print("Lines are identical.....")
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    fname = os.path.isfile(filename)

    try:
        if fname == True:
            my_list = open(filename, 'r').read().splitlines()
            print(my_list)
            return my_list
    except FileNotFoundError:
        print("File does not exist!")


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    NODIFF = "No differences\n"

    my_list1 = get_file_lines(filename1)
    my_list2 = get_file_lines(filename2)

    line_num, index = multiline_diff(my_list1, my_list2)
    if line_num == -1:
        print("No Differences\n")
        return NODIFF
    if line_num == 0 and index == 0:
        if my_list1 == []:
            line1 = ""
            line2 = my_list2[line_num]
            semifinal_answer = singleline_diff_format(line1, line2, index)
            final_answer = "Line " + str(line_num) + ":\n" + str(semifinal_answer)
            return final_answer
        elif my_list2 == []:
            line2 = ""
            line1 = my_list1[line_num]
            semifinal_answer = singleline_diff_format(line1, line2, index)
            final_answer = "Line " + str(line_num) + ":\n" + str(semifinal_answer)
            return final_answer
    print("Diff detected!\n Line#: " + str(line_num) + "\n Index: " + str(index))
    line1 = my_list1[line_num]
    line2 = my_list2[line_num]
    semifinal_answer = singleline_diff_format(line1, line2, index)
    final_answer = "Line " + str(line_num) + ":\n" + str(semifinal_answer)

    print(final_answer)
    return final_answer



# Owltest Code

# idx00 = singleline_diff('a', 'b')
#
# singleline_diff_format("abc", "abc", -1)
# singleline_diff_format("abc", "abd", 2)
# singleline_diff_format("bc", "abc", 0)
# singleline_diff_format('abcdefg', 'abc', 5)
# singleline_diff_format('Python is fast!!!', 'Python is fun!!!', 11)
# singleline_diff_format('abc', 'abd', 2)
# singleline_diff_format('', 'a', 0)

# lines1 = ["one", "two", "three"]
# lines2 = ["one", "four", "three"]
# multiline_diff(lines1, lines2)
# multiline_diff(['a'], ['b'])
# multiline_diff(['line1', 'line2'], ['line1', 'lne2'])
# multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3'])
# multiline_diff(['line1', 'line2'], ['line1', 'line2'])


# get_file_lines('file1.txt',)
#
# file_diff_format('file1.txt', 'file2.txt')
# file_diff_format('file1.txt', 'file1.txt')
# file_diff_format('file9.txt', 'file9.txt')
file_diff_format('file8.txt', 'file9.txt')

# Bryant's Tests


# idx01 = singleline_diff("abcd", "abcd")
# idx02 = singleline_diff("abdc", "abcd")
# idx03 = singleline_diff("abcd", "abc")
# idx04 = singleline_diff("abc", "abbc")
#
# # singleline_diff_format("abcd", "abcd", idx01)
# singleline_diff_format("abdc", "abcd", idx02)
# singleline_diff_format("abcd", "abc", idx03)
# singleline_diff_format("abc", "abbc", idx04)

# singleline_diff_format("abcd", "abcd", [50])
