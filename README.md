# ACM Quantum Github Tutorial

## Table of Contents
  - [Install Software](#install-software)
  - [Set Up SSH Authentication](#set-up-ssh-authentication)
  - [OS Specific Instructions](#os-specific-instructions)
    - [Windows](#windows)
    - [MacOS](#macos)
      - [Special MacOS Instructions](#special-macos-instructions)
    - [Linux (NOT WSL)](#linux-not-wsl)


### Install Software

**Please skip to the section below that corresponds with your operating system.**

Once you finish installation, move on to setting up SSH authentication.
- [Windows](#windows)
- [macOS](#macos)
- [Linux (NOT WSL)](#linux-not-wsl)

Once you have successfully completed the above steps **please make sure to come back here to complete the remaining steps!**

### Set Up SSH Authentication

**If you are on Windows, do the key setup and clone in WSL. NOT in Powershell/CMD**

These instructions work for all operating systems.
1. Open Terminal
2. Paste `ssh-keygen -t ed25519 -C "your_email@example.com"`, substituting your GitHub email address (terpmail and personal both work)
3. When you're prompted to "Enter a file in which to save the key", you can **press Enter to accept the default file location**. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key. If this is the case, press `ctrl + c` to cancel the generation, you already have a key.
4. At the prompt, type a secure passphrase. I prefer something short - you will be typing this a lot. A weak password is a hell of a lot better than no password.

You have now created a public/private key pair located at `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub`

Next, we will add your public key to your GitHub account

5. Run `cat ~/.ssh/id_ed25519.pub` and copy the public key that is displayed.
6. Go to [https://github.com/settings/keys](https://github.com/settings/keys)
7. Click "Add a new SSH key"
8. Paste in your copied public key, it should look like: `ssh-ed25519 <64 characters of hash> <your email>`
9. Add the key. You can now authenticate this computer to GitHub using SSH. 

Optional: If you do not want to type the password every time you push/pull [Use `ssh-add` to add the key to the SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?#adding-your-ssh-key-to-the-ssh-agent) If you are on windows, use the Linux instructions in WSL. Do not continue to the hardware security key section.

## OS Specific Instructions
### Windows

*This will only work on Windows 10 and newer.  If you are on an older version, you will probably need to set up a Linux VM.*

**All instructions (except 1) must be executed within WSL, NOT in Powershell**

1. Follow the directions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install the Windows Subsystem for Linux
2. Make sure you are on WSL 2 with [this test](https://learn.microsoft.com/en-us/windows/wsl/install#check-which-version-of-wsl-you-are-running)
3. Install the basic dependencies:
    - Run:
      ```
      sudo apt update && sudo apt upgrade -y
      sudo apt install -y git python3 python3-venv python3-pip
      python3 -m venv ~/.venvs/qiskit
      source ~/.venvs/qiskit/bin/activate
      python3 -m pip install -U pip
      python3 -m pip install qiskit
      ```
4. Jump back to [Set Up SSH Authentication](#set-up-ssh-authentication) to complete the remaining steps for this project.

### MacOS

Check the [Special macOS Instructions](#special-macos-instructions) to check if you need to follow any special steps. **Then**, come back here.

0. Update your operating system (optional but recommended)
1. Install the Homebrew package manager
    - Run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    - **if you're prompted with instructions to add Homebrew to your PATH, copy and paste the three commands provided by the terminal after running the above command**
2. Install the basic dependencies
    - Run:
      ```
      brew install python
      python3 -m venv ~/.venvs/qiskit
      source ~/.venvs/qiskit/bin/activate
      python3 -m pip install -U pip
      python3 -m pip install qiskit
      ```
3. Jump back to [Set Up SSH Authentication](#set-up-ssh-authentication) to complete the remaining steps for this project.

#### Special MacOS Instructions

Check to see if you're running an older version of macOS. Either click the Apple button in the menubar in the top-left and click "About This Mac", or else run `sw_vers` from the terminal. You should only need the special section if your macOS version is less than 10.15

If your macOS version is less than 10.15, follow [the directions for macOS](#macos), but with the changes listed below. Otherwise, ignore the following section.

- If you have run the special instructions in previous classes or semesters, undo by uninstalling homebrew:
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"`
  - You will probably have leftover files in `/opt/homebrew` or `/usr/local`. We will *try* to help you delete them in OH.
- Afterwards, run `brew install qiskit`

### Linux (NOT WSL)

These instructions assume you have a Debian-based system (e.g. Ubuntu) using the Bash shell.  If you have a different distribution, you will have to find and download the corresponding packages in your native package manager. Note that the packages there may have slightly different names. Note that commands that modify `.bashrc` will need to be changed to modify your respective `.rc` file.

1. Firstly, install the basic dependencies:
    - Run `sudo apt update` to update your local package listing
    - Run:
      ```
      sudo apt update
      sudo apt install -y git python3 python3-venv python3-pip
      
      python3 -m venv ~/.venvs/qiskit
      source ~/.venvs/qiskit/bin/activate
      
      python3 -m pip install -U pip
      python3 -m pip install qiskit
      ```
3. Jump back to [Set Up SSH Authentication](#set-up-ssh-authentication) to complete the remaining steps for this project.
