# Task 5.2

### 1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are present in it, what users exist on the system? Specify several pseudo-users, how to define them?

For example it contains:
`user:x:1000:1000::/home/user:/bin/bash`
It means:
 - there is a user named "user".
 - user has password stored in `/etc/shadow`;
 - the UID and GID are `1000`;
 - home directory is `/home/user`;
 - user's shell is `/bin/bash`.

### 2) What are the uid ranges? What is UID? How to define it?

UID is the user identificator. To check the UID we can use `id` command:

```console
$ id user
uid=1000(user) gid=1000(user) groups=1000(user),108(vboxusers),977(docker),986(video),995(audio),998(wheel)
```

UID ranges:
- UID 0 (zero) is reserved for the root.
- 1…999 → System users. These are users that do not map to actual “human” users, but are used as security identities for system daemons, to implement privilege separation and run system daemons with minimal privileges.
- 65534 → The nobody UID, also called the “overflow” UID or similar.
- 65535, aka “16bit (uid_t) -1” → Before Linux kernel 2.4 uid_t used to be 16bit, and programs compiled for that would hence assume that (uid_t) -1 is 65535. This UID is hence not usable either.
- 1000…65533 and 65536…4294967294 → Everything else, i.e. regular (human) users.

UID ranges may vary from a distribution to distribution and can be changed in `/etc/login.defs`.

We can change the UID of the user using this command: `usermod -u 1002 user`. Then we should update the owning files to support the new user: `find / -uid 1000 -exec chown -v -h 900 '{}' \;`.

### 3) What is GID? How to define it?

GID is the group identifier. Like UID, GID 0 is reserved for root group, the first 100 UIDs are reserved for system use.

Changing GID for `group01` group: `groupmod -g 600 group01`. Then change owning files: `find / -gid 700 -exec chgrp -v 600 '{}' \;`

### 4) How to determine belonging of user to the specific group?

The commands are `id username` and `groups username`.

### 5) What are the commands for adding a user to the system? What are the basic parameters required to create a user?

The command are `useradd` and `adduser` utilities. `adduser` is user-friendly utility for debian/ubuntu, `useradd` is more low level.

Here are some important parameters for `useradd`:
- -G - specify groups;
- -m - create home directory;
- -d - specify home directory;
- -u - specify UID;
- -g - specify specific initial login group;
- -s - specify shell.

### 6) How do I change the name (account name) of an existing user?

Renaming user:
- with username: `usermod -l new-name old-name`;
- with UID: `usermod -u UID new-name`

Note: we need to kill all processes used by the user to rename them

### 7) What is skell_dir? What is its structure?

skell_dir is used to generate a new home directory for user. It''s `/etc/skell` by default, but can be changed in the `/etc/default/useradd`.

### 8) How to remove a user from the system (including his mailbox)?

User can be deleted using `userdel` command. For example, to delete a user, their home directory and their mailbox `userdel -r username`. Note that all user's process must be stopped, otherwise use `-f (--force)` parameter.

### 9) What commands and keys should be used to lock and unlock a user account?

There are two ways to lock user from command line:
- passwd -l username;
- usermod -l username.

As well as two ways to unlock:
- passwd -u username;
- usermod -U username.

### 10) How to remove a user's password and provide him with a password-free login for subsequent password change?

The command is `userdel -d username`.

### 11) Display the extended format of information about the directory, tell about the information columns displayed on the terminal.

```console
jenneron@xe503c12:~/git/DevOps_online_Kyiv_2021Q4$ ls -l
total 20
drwxr-xr-x 3 jenneron jenneron 4096 Jan  4 01:45 m1
drwxr-xr-x 4 jenneron jenneron 4096 Jan  4 01:45 m2
drwxr-xr-x 3 jenneron jenneron 4096 Jan  4 01:45 m3
drwxr-xr-x 3 jenneron jenneron 4096 Jan  4 01:45 m4
drwxr-xr-x 4 jenneron jenneron 4096 Jan  4 01:49 m5
```

For example let's take this string:
```console
drwxr-xr-x 3 jenneron jenneron 4096 Jan  4 01:45 m1
````
So:
- `drwxr-xr-x` is permissions;
- `3` is amount of hard links;
- `jenneron` is user name;
- `jenneron` is group name as well;
- `4096` is the size in bytes;
- `Jan  4 01:45` is modification date;
- `m1` is the name;

### 12) What access rights exist and for whom (i. e., describe the main roles)? Briefly describe the acronym for access rights.

User rights consist of 3 blocks:
- 3 bits of owner's rights;
- 3 bits of group owners' rights;
- 3 bits of everyone else's rights.

For example:
```console
drwxr-xr-x 3 jenneron jenneron 4096 Jan  4 01:45 m1
```
The rights are `rwxr-xr-x` so we have 3 blocks:
- `rwx` means the owner can read, write and execute;
- `r-x` means the group members can read and execute;
- `r-x` means that everyone else can read and execute as well.

### 13) What is the sequence of defining the relationship between the file and the user?

User's rights, group members' and then others'.

### 14) What commands are used to change the owner of a file (directory), as well as the mode of access to the file? Give examples, demonstrate on the terminal.

The command to change the mode of access is `chmod`. For example:
```console
jenneron@xe503c12:~/test$ ls -l file
-rw-r--r-- 1 jenneron jenneron 0 Jan  4 03:44 file
jenneron@xe503c12:~/test$ chmod 777 file # give all permissions
jenneron@xe503c12:~/test$ ls -l file
-rwxrwxrwx 1 jenneron jenneron 0 Jan  4 03:44 file
Try 'chown --help' for more information.
jenneron@xe503c12:~/test$ chmod -x file # remove executing permissions
jenneron@xe503c12:~/test$ ls -l file
-rw-rw-rw- 1 jenneron jenneron 0 Jan  4 03:44 file
```

The command to change the owner is `chown`. For example
```console
jenneron@xe503c12:~/test$ sudo useradd test_user
jenneron@xe503c12:~/test$ sudo chown test_user file
jenneron@xe503c12:~/test$ ls -l file
-rw-rw-rw- 1 test_user jenneron 0 Jan  4 03:44 file
```

### 15) What is an example of octal representation of access rights? Describe the umask command.

Each permission may be specified with an octal number: read = 4; write = 2; execute = 1; no permission = 0. The octal equivalents are derived by adding the numbers associated with the four basic permissions. The following table illustrates their use:

| Octal number | Symbolic | Permission         |
| ------------ | ---------| ------------------ |
| 0            | ---      | none               |
| 1            | --x      | execute            |
| 2            | -w-      | write              |
| 3            | -wx      | write/execute      |
| 4            | r--      | read               |
| 5            | r-x      | read/execute       |
| 6            | rw-      | read/write         |
| 7            | rwx      | read/write/execute |

`umask` is a utility which reads and sets default mask of file (default permissions). `umask` affects only the current shell environment. On most Linux distributions, the default system-wide umask value is set in the pam_umask.so or /etc/profile file.

To check the umask value:
```console
jenneron@xe503c12:~/test$ umask
0022
```

The default permissions for files are 666 (read and write), for directories are 777 (read, write, execute). Let's calculate the umask of 0022 for these cases:
- for files it will be 666 - 022 = 644;
- for directories it will be 777 - 022 = 755

To check the umask in symbolic notation:
```console
jenneron@xe503c12:~/test$ umask -S
u=rwx,g=rx,o=rx
```

The example of setting umask value: `umask 027`.

### 16) Give definitions of sticky bits and mechanism of identifier substitution. Give an example of files and directories with these attributes.

Sticky bit is a special permission which prevents directory from being removed by anyone except the owner and root.

The example of sticky bit usage is `/tmp` directory.

### 17) What file attributes should be present in the command script?

Command script should have `x` (executable) attribute.
