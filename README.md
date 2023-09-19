# Beginners-Track
## Repository for the beginner's track. **Make your own branch for this repo and name it `team/<teamname>`** before your sub-team starts working

### Overview
- There is a folder for backend and frontend each. There's separate read me files for each of them.
- Edit this file to add your name and github username to the list below

### Set up

1. Create a new folder for this repo
2. Fork this repo
    - Click on the fork button on the top right
    - Select your github account
    - Click on the clone button and copy the link
3. Clone the repo into the folder
    - `git clone git@github.com:ECLAIR-Robotics/Beginners-Track.git`
4. Follow the instructions in the backend and frontend read me files to set up the backend and frontend

### Important Links

- [Notion](https://befitting-galliform-d9c.notion.site/Teamspace-Home-55272a58604e4c698ee3448da03d4a08?pvs=4)

### Important Commands

- `git pull` - Pulls the latest changes from the repo
- `git add .` - Adds all the files you have changed to the commit
- `git commit -m "commit message"` - Commits the changes you have made
- `git push` - Pushes the changes to the repo
- `git checkout -b <branch name>` - Creates a new branch and switches to it
- `git checkout <branch name>` - Switches to the branch
- `git branch` - Shows all the branches
- `git merge <branch name>` - Merges the branch into the current branch
- `git branch -d <branch name>` - Deletes the branch
- `git status` - Shows the status of the repo
- `git log` - Shows the commit history
- `git reset --hard <commit hash>` - Resets the repo to the commit
- `git reset --hard origin/<branch name>` - Resets the repo to the remote branch
- `git reset --hard HEAD^` - Resets the repo to the previous commit
- `git reset --hard HEAD^^` - Resets the repo to the commit before the previous commit
- `cd` - Change directory
- `ls` - List files in the current directory
- `cd ..` - Go back one directory
- `cd <folder name>` - Go into the folder
- `mkdir` - Make a new folder
- `rm -rf <folder name>` - Delete a folder
- `rm <file name>` - Delete a file

### SSH instructions

***RPI.GPIO libraries don't run unless you run them on a Raspberry Pi. So you will have to SSH into a Raspberry Pi to test the code.***

**Only for the first Time**

- `ssh testuser@<ip address>` - SSH into the Raspberry Pi
- `sudo useradd -m <username>` - Create a new user based on your team name
- `sudo passwd <username>` - Set a password for the user
- `sudo usermod -a -G sudo <username>` - Add the user to the sudo group
- `mkdir <teamname>` - Make a new folder
- `cd <teamname>` - Change directory
- `git clone git@github.com:ECLAIR-Robotics/Beginners-Track.git` - Clone the repo

**For every time next time**

- Use the VS Code SSH extension to connect to the Raspberry Pi
- Use the open folder option to open the folder you cloned the repo into
- Use the terminal in VS Code to run the code


_INSERT LEAD NAME HERE_

**Team Members**
_INSERT NAME HERE_



