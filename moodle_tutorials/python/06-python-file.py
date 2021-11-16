def main():

  """ Create, Write and Close File """

  # 01. Open a file for writing and create it if it doesn't exists

  file_01 = open("text-01.txt", "w+")

  # 02. Write some lines of data to the file / or overwrite content data

  for i in range(10):
    file_01.write("This is line " + str(i) + "\r\n")

  # 03. Close the file when done

  file_01.close()

  """ Create, Append (a) content, Write and Close File """

  file_02 = open("text-01.txt", "a")

  for i in range(10):
    file_02.write("This is line " + str(i) + "\r\n")

  file_02.close()


  """ Read (r) and write files using the built-in Python methods """

  # 01. Open file with "read" (r) argument

  file_03 = open("text-01.txt", "r")

  # 02. Check if file is open and ready for reading

  if file_03.mode == "r":
    # 03_a. If the file mode is set to "read" (r) then read file
    """ contents = file_03.read()
    print (contents) """

    # 03_b. Or, read file content with read lines
    file_lines = file_03.readlines()
    for line in file_lines:
      print(line)

if __name__ == "__main__":
  main()