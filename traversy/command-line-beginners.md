The **Shell** is the program that the terminal runs on. **Bash** in the default on most linux systems and it was the default for a long time on Mac until they switched to **zsh**

To rename files and folders, use the **mv** command. Even though this is the move command, this will take the file and "move" it to the new name. For example, to rename a file or folder called source to src, you would do `mv source src`

The **cat** command can be used to view the contents of a file as well as write to the file. To view the contents of a file, we'd do `cat info.txt`. To write to a file, we could do `cat > info.txt` to drop us into an editor. However, we'll likely use **nano** to quickly edit from the command line.

**nano** can show linenumbers of a file by using the `-l` switch like `nano -l readme.txt`![image](https://user-images.githubusercontent.com/7660667/194983299-63448daf-eddb-4348-b342-ba4dacffd30b.png)

You can use the **touch** command to generate a bunch of files at once rather than just one at a time. For example, `touch file-{001...100}.txt` will generate 100 files named `file-001.txt` all the way to `file-100.txt`

You can use the **find** command instead of grep to do something like find all files where the text is empty with `find . -empty`. We can also use this command to find files of a certain naming scheme with `find . -name "file-00*.txt`

**history** is a command that will give you a history of commands that you've run and then you can use `[cmd number]` to run the command in your history. For example, I can run `history` and then `!5745` to redo the `ls` command. This is *very* useful and more efficient than using the arrow keys
