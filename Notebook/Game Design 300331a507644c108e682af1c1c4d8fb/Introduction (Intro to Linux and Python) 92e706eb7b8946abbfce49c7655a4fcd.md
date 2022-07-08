# Introduction (Intro to Linux and Python)

Linux Commands:

pwd (print working directory)
ls (list contents)
mkdir (make dirrectory)
cd (change directory)
cd .. (takes you to the previous directory)

go to the tab key to autofill directory or file names

mv (filename) (new_filename)
cp (copy)
ex: cp (filename) (new_filename)

- rule of thumb: don't use spaces in file names

rm (delets file) - dangerous tool. can't undo

apt list --upgradeable to see packages that can be upgraded

rm -rf is a recursive delete that removes everything up the file path.

(WARNING) - don't run commands you don't have mastery over with sudo. sudo can really mess things up.
(sudo means super user do)

mkdir: creates a directory
rmdir: deletes directoy

additional tips:
shell is infinitely configurable.

ctrl r will search backwords in your history.
you can use the arrow keys to go forwads and backwards in your history
if you have bash, you can read the book to learn how to customize everything
vim uses bash to move around

- in bash the goal is to find the keyboard shortcuts you're comfortable (or invent them) to make coding/working faster

it's all about saving time.

code (name of file): opens up file in visual studio code

python3 (filename): runs a file

so:

- -------------python file start:-------------------
""" every module needs a docstring"""

def main():
"""every file needs a docstring"""

if **name** == '**main**':
main()

is the basic start for a python file.
you need to start your program here, and move

once you create a file, run it through pylint to ensure program is pythinic

so:
python3 is interactive.

type python3

now you're in a python terminal

imagine you want to do some math:

import math
31.5 * math.sqrt(2)

- outputs the sqrt of 31.5

gives you  the sqty of the file

installing a program:

ssh ersatz - log into lunix system.

apt search pylint
searches for a program named pylint to install

sudo apt install (file name)
it asks you for the password
it won't provide feedback when you're typing the password, just know it's typeing

shabang

#! /usr/bin/env pyhton3

# line 1 is the shebang

- > this tells the operating system that the file is python3

chmod ugo+x (filename)

chmod = changemod
ugo+x adds executible

ls -l shows you

chmod ugo-x removes executible permissions from file

((((FOR ME))))
remember to add a troubleshooting note file for things like:

- what if you're missing a shebang? what does that look like?
- virtual machines
vmware
vagrant
- setting up my wifi -
jacob@SpecterUbuntu:/lib/firmware$ tar tzf ~/Downloads/iwlwifi-qu-48.13675109.0.tgz
iwlwifi-Qu-48.13675109.0/
iwlwifi-Qu-48.13675109.0/iwlwifi-Qu-b0-jf-b0-48.ucode
iwlwifi-Qu-48.13675109.0/iwlwifi-Qu-c0-jf-b0-48.ucode
iwlwifi-Qu-48.13675109.0/README.iwlwifi-Qu.ucode
iwlwifi-Qu-48.13675109.0/iwlwifi-Qu-c0-hr-b0-48.ucode
iwlwifi-Qu-48.13675109.0/iwlwifi-Qu-b0-hr-b0-48.ucode
iwlwifi-Qu-48.13675109.0/LICENSE.iwlwifi-Qu.ucode
jacob@SpecterUbuntu:/lib/firmware$ sudo tar xzf ~/Downloads/iwlwifi-qu-48.13675109.0.tgz
[sudo] password for jacob:
Sorry, try again.
[sudo] password for jacob:
Sorry, try again.
[sudo] password for jacob:
sudo: 3 incorrect password attempts