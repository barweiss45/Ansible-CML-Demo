# CML - Anisible Scripts
Playbooks and scripts for my internal CML test bed in the lab.

## Notes on Some Caveats
You may need to make changes your .ssh/config file due to IOSv not accepting some of the newer ssh key algorithms. This can be remediated by creating a .ssh/config file if this does not already exist or updating it if it does existing. It is also suggested to turn StrictHostKeyChecking off when using IOSv and ansible. This is an example of the configuration:
```
# Assuming that you do not have a ~/.ssh/config file in your home directory.
touch ~/.ssh/config
cd ~/.ssh/

# Use your favorite editor (e.g. Vim, Nano, etc.)
Host <IP or Regex>
    KexAlgorithms +diffie-hellman-group14-sha1
    StrictHostKeyChecking no
```