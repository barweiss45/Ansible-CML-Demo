# CML - Anisible Scripts
Playbooks and scripts for my internal CML test bed in the lab.

# About the Lab Enviroment
For this lab I used an Ubuntu 20.04.3 LTS VM and CML. The Ubuntu VM housed all my services such as Ansible, SCP, TFTP (for ZTP), and DHCP for my lab. CML ran on the same host as my Ubuntu VM and were connected by a layer 3 bridge allowing me to use an out of band network (OOB) to access the network devices that ran in CML. However, in order to run this enviromenment you do not have to use the same design. 

:thumbsup: In fact this lab can be replicated on the DevNet Sandbox's Cisco Modeling Labs Enterprise instance. [Click here](https://devnetsandbox.cisco.com/RM/Topology) and then type CML in the search box in the upper lefthand side. See screen cap below
![DevNet Sandbox Screen Cap GIF](https://lucid.app/publicSegments/view/c198f660-c64b-46dc-901a-636d4638187c/image.png)


## Lab Topology
![Lab Topology on Lucidcart](https://lucid.app/publicSegments/view/622eb251-d6a7-422f-a36b-da2c68a4e2bc/image.png)

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