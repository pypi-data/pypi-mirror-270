Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Applications\{dekshell_exe}]

[HKEY_CLASSES_ROOT\Applications\{dekshell_exe}\shell]

[HKEY_CLASSES_ROOT\Applications\{dekshell_exe}\shell\open]

[HKEY_CLASSES_ROOT\Applications\{dekshell_exe}\shell\open\command]
@="\"{path_dektools_full_path}\" cmd admin {dekshell_exe} rf \"%1\""
