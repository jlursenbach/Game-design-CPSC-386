# Intro to GitHub

## PAT:

Create a personal access token

- GitHub > Settings > Developer Settings (bottom of list on left) > Personal Access Tokens
    - Set expiration -
    - select scopes:
        - repo is a requirement
        - (click all boxes if you want)
    
    at the bottom of the page: Generate Token
    
    Remember to copy the token (it’s only ever shown/provided once. Copy it, save it)
    

command: 

wget -q [https://raw.githubusercontent.com/mshafae/tusk/main/gcf](https://raw.githubusercontent.com/mshafae/tusk/main/gcf) .sh

wget - grabs somethign from internet

-q (switch tells it to be quiet)

a code url

.sh - runs it through the bash shell

if you don’t have wget installed

now: answer the questions

Than it will build a library etc. waot paitently

your password is your PAT

sometimes students will go to GitHub and not see what we’re working on 

search or type → remember we don’t own the repo. 

→ we can bookmark the URL

→ or go to canvas and follow the links to our homework assignment

github.com/mshafae-summer-2022

to clone the repo:

git clone (https from github)

than provide username and PAT you made above. 

## SSH

## Github Commands

git status : checks github status

mate  sqrt_program.py 

> mate calls the ide
> 

→ create program save it to computer

git add (filename)

git commit 

→ takes you to vim. you COULD use vim. to escale → <esc> <esc> <esc> :q 

git commit -m “(type a message here)”

git push : has to come after commit to get onto the web

git commit -a -m (”commit message”)