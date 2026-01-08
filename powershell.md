You can download the newest versions from [https://github.com/PowerShell/powershell](https://github.com/PowerShell/powershell)

powershell can be used now with vscode considering it is multi platform

**alias** are shortened forms of longer commands and can be used is the console. The full command should be used in a script to avoid confusion. You can get all available aliases with `get-alias`

## Three essential commands

Three commands that are essential for learning a powershell command without needing to use a search engine are
```powershell
get-command
get-help
get-member
```

To look for commands that include get as the verb and use something with dns, we can use
```powershell
get-command -verb get -noun *dns*
```

To find help with specific commands, we can use get-help

```
get-help -name get-command
```

Or if you want to see all the commands that might apply

```
get-help -name *dns*
```

and then use the detailed flag for a description

```powershell
get-help -name set-dnsclient -detailed
```

which is the equivalent to man pages in linux

update the help files with

```powershell
update-help
```

To see examples of how to use the commands **very useful**

```
get-help -name get-command -examples
```

You may need to update the help files first

### About File

About files are a concept in powershell of how to find out about the help file

```powershell
help *about*
```

will get all of the about files
