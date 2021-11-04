# CML - Anisible Scripts
## Introduction
Playbooks and scripts for my internal CML test bed in the lab.

## Before starting this walkthrough, these are the skills you should have
* a basic knowledge of navigating the Linux Bash Sheel (although you can run this lab on MacOS or Windows, it is easier to do much of this in an Linux environment).
* a rudimentry knowledge of Python or some basic programming knowledge
* understand data encoding structures such as JSON and YAML (especially YAML!)
* a Cisco Modeling Lab (CML) configured and host machine that can access your network devices on the CML instance. You will need to set up external connectivity with a bridge interface on CML to do this.

## About the Lab Enviroment
For this lab I used an Ubuntu 20.04.3 LTS VM and CML. The Ubuntu VM housed all my services such as Ansible, SCP, TFTP (for ZTP), and DHCP for my lab. CML ran on the same host as my Ubuntu VM and were connected by a layer 3 bridge allowing me to use an out of band network (OOB) to access the network devices that ran in CML. However, in order to run this enviromenment you do not have to use the same design. 

:thumbsup: BONUS: In fact this lab can be replicated on the DevNet Sandbox's Cisco Modeling Labs Enterprise instance. [Click here](https://devnetsandbox.cisco.com/RM/Topology) and then type CML in the search box in the upper lefthand side. See screen cap below to see how to get to the sandbox (NOTE: you will need to have to sign in or sign up if you are not already registered with developer.cisco.com):
![DevNet Sandbox Screen Cap GIF](/assets/images/devnet_sandbox.gif)
Just be aware there are some extra steps you may need to do. Maybe I'lll add those instructions later.

## Before you start
1. Ensure that your envirorment has ```git``` installed. If not there are plenty of tutorials that can walk you through this installation process on your host. Just google 'How do I install git for my environment?'

2. Python should be installed. I used Python 3.6.10 during the creation of this walkthrough; however, check the documentation to be sure you are using the correct version to run ansible. I also highly recommend that you use ```pyenv``` to set up python environment. Please see this [tutorial](https://github.com/barweiss45/my-pyenv-guide) that I created that will walk you though setting up ```pyenv```.

3. Clone this repostitory in your home directory. For example:
    ```
    mkdir Ansible-CML
    git clone https://github.com/barweiss45/Ansible_CML.git Ansible-CML
    cd Ansible-CML
    ```
4. Install the ```requirements.txt``` file located in the Ansible-CML directory with ```pip```.
    ```
    pip install -f requirements.txt
    ```
5. Verify

## Setting up Ansible

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