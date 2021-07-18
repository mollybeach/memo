
#look
ls — List directory contents.
less — view the contents of a text file
grep — search.
locate — Locate a specific file or directory
echo — Prints text to the terminal window.


#directory 
touch — Creates a file.
mkdir — Create a directory.
pwd — Print working directory.
mv — Move or rename directory
rmdir — Remove directory
cp — copy files and directories [cp [option(s)] current_name new_name]


#read
cat — Read a file, create a file, and concatenate files
head — Read the start of a file
tail — Read the end of a file


#redirect
> — redirect stdout
| — Pipe A pipe takes the standard output of one command and passes it as the input to another.


#command info 
man — Print manual or get help for a command.
history — list your most recent commands
compgen — Shows all available commands, aliases, and functions


#end 
exit — Exit out of a directory
clear — Clear your terminal window
kill — terminate stalled processes [ kill [signal or option(s)] PID(s)]
sleep — delay a process for a specified amount of time [sleep number [suffix]]


#permission
sudo-  allows a permitted user to execute a command as the superuser or another user

chmod — Sets the file permissions flag on a file or folder

 [chmod [option(s)] permissions file_name]
There are situations that you’ll come across where you or a colleague will try to upload a file or modify a document and you receive an error because you don’t have access. The quick fix for this is to use chmod. Permissions can be set with either alphanumeric characters (u, g, o) and can be assigned their access with w, r, x. Conversely, you can also use octal numbers (0-7) to change the permissions. For example, chmod 777 my_file will give access to everyone.

