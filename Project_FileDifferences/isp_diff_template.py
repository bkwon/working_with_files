"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

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
        print("Line 1 is shorter and this is the length: " + str(len(line1)))
        line1, line2 = line2, line1

    for letter in range(len(line1)):
        try:
            print("Iteration: " + str(letter))
            if line1[letter] != line2[letter]:
                print("Lines differ at position {}".format(letter))
                # print(i, line1[i], line2[i])
                # print("1st diff is at index = " + str([i]))
                return [letter]

        except IndexError:
            print("Lines differ at catch position {}".format(letter))
            return [letter]
    else:
        print("The lines are identical")
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

    print()
    print(line1)
    sep = ('=' * len(line1))
    print(sep)
    print(line2 + "\n")
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


# def main():
# singleline_diff("abcd", "abcd")
print("HERE")
idx02 = singleline_diff("abdc", "abcd")
print(idx02)
# singleline_diff("abcd", "abc")
# singleline_diff("abc", "abbc")

# singleline_diff_format("abcd", "abcd", singleline_diff("abcd", "abcd"))
singleline_diff_format("abdc", "abcd", idx02)
# singleline_diff_format("abcd", "abc", None)
# singleline_diff_format("abc", "abbc", None)