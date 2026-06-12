# Now we gonna cover write ---> 'w' mode 
#Delete the old content and write a new content

f = open("example_1.txt", 'w')
f.write("change and write the new text\n")
f.write("i change the new line, "
"and here is the best part , "
"if you can't change the mode you can change the dist ofcourse .")

f.close() 