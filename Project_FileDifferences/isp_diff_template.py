"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import itertools

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

    else:
        # print("Identical here")
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
    # list1 = list(enumerate(lines1))  # using enumerate to add enumeration for each element of list
    # list2 = list(enumerate(lines2))

    # for lineidx, line1 in enumerate(lines1):
    for lineidx, line1 in enumerate(itertools.zip_longest(lines1, lines2)):
        # print("{}:{}".format(lineidx, line1))
        # line1 = lines1[lineidx]
        # line2 = lines2[lineidx]
        # print(line1)
        # print(line2)
        try:
            # if lines1[lineidx] != lines2[lineidx]:
            line1 = lines1[lineidx]
            line2 = lines2[lineidx]
            index = singleline_diff(line1, line2)
            if index != -1:  # need an if identical but not done with list logic here
                # for index in range(len(lines1)):
                print("Got here!")
                print(lineidx, index)
                return (lineidx, index)

            # print("Lines are identical!")
            # return (IDENTICAL, IDENTICAL)

        except IndexError:
            print("Got index error!! --> (" + str(lineidx) + ", 0)")
            return (lineidx, 0)

    print("Lines are identical.....")
    return (IDENTICAL, IDENTICAL)


    # print("List1 at index0 = " + str(list1[0]))
    # print("Length of List 1 is: " + str(len(lines1)))
    # if list1 != list2:
    #     print("Lists are different!")
    #
    # print(list1 + list2)
    # print(list1[0])
    # print("Returning (IDENTICAL, IDENTICAL)")
    # return (IDENTICAL, IDENTICAL)


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
    return []


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
    return ""


"""
Owltest Code
"""
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
multiline_diff(['line1', 'line2'], ['line1', 'lne2'])
multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3'])
multiline_diff(['line1', 'line2'], ['line1', 'line2'])

"""
Bryant's Tests
"""

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
