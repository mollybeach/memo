ls — List directory contents.
echo — Prints text to the terminal window.
touch — Creates a file.
mkdir — Create a directory.
grep — search.
man — Print manual or get help for a command.
pwd — Print working directory.
mv — Move or rename directory
rmdir — Remove directory
locate — Locate a specific file or directory
less — view the contents of a text file
compgen — Shows all available commands, aliases, and functions

> — redirect stdout
cat — Read a file, create a file, and concatenate files
| — Pipe A pipe takes the standard output of one command and passes it as the input to another.

head — Read the start of a file
tail — Read the end of a file
chmod — Sets the file permissions flag on a file or folder

There are situations that you’ll come across where you or a colleague will try to upload a file or modify a document and you receive an error because you don’t have access. The quick fix for this is to use chmod. Permissions can be set with either alphanumeric characters (u, g, o) and can be assigned their access with w, r, x. Conversely, you can also use octal numbers (0-7) to change the permissions. For example, chmod 777 my_file will give access to everyone.

Syntax: chmod [option(s)] permissions file_name

Common options: -f, -v

exit — Exit out of a directory

The exit command will close a terminal window, end the execution of a shell script, or log you out of an SSH remote access session.

Syntax: exit

Common options: n/a


Keep the learning going.
Learn Bash without scrubbing through videos or documentation. Educative’s text-based course is easy to skim and features live coding environments - making learning quick and efficient.

Master the Bash Shell


history — list your most recent commands

An important command when you need to quickly identify past commands that you’ve used.

Syntax: history

Common options: -c, -d

clear — Clear your terminal window

This command is used to clear all previous commands and output from consoles and terminal windows. This keeps your terminal clean and removes the clutter so you can focus on subsequent commands and their output.

Syntax: clear

Common options: n/a

cp — copy files and directories

Use this command when you need to back up your files.

Syntax: cp [option(s)] current_name new_name

Common options: -r, -i, -b

kill — terminate stalled processes

The kill command allows you to terminate a process from the command line. You do this by providing the process ID (PID) of the process to kill. To find the PID, you can use the ps command accompanied by options -aux.

Syntax: kill [signal or option(s)] PID(s)

Common options: -p

sleep — delay a process for a specified amount of time

sleep is a common command for controlling jobs and is mainly used in shell scripts. You’ll notice in the syntax that there is a suffix; the suffix is used to specify the unit of time whether it be s (seconds), m (minutes), or d (days). The default unit of time is seconds unless specified.

Syntax: sleep number [suffix]

Common options: n/a

