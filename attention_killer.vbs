Set objShell = CreateObject("WScript.Shell")
objShell.Run "python """ & CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName) & "\attention_killer.py""", 0, False
Set objShell = Nothing