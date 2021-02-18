# Competitive Programming

## Setting up an M1 Mac
1.  To install Command Line Tools, enter the command `xcode-select --install` in Terminal
2.  To install Rosetta 2, enter the command `softwareupdate --install-rosetta` in Terminal
3.  To run an x86 Terminal, rename a duplicated Terminal to Terminal Rosetta, navigate to its Get Info window using Command-I, and enable `Open using Rosetta` 

## Setting up Homebrew (use an x86 Terminal for M1 Macs)
1. To install [Homebrew](https://brew.sh), enter the command `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` in Terminal
2. To disable Homebrew analytics tracking, enter the command `brew analytics off` in Terminal
3. To update Homebrew and all currently installed packages, enter the command `brew update && brew upgrade` in Terminal
4. To remove old cache and log fiels, enter the command `brew cleanup` in Terminal

## Setting up GCC and bits/stdc++.h (use an x86 Terminal for M1 Macs)
1. To install GCC using Homebrew, enter the command `brew install gcc` in Terminal
2. To precompile the bits/stdc++.h header file, enter the command `g++-10 -std=c++17 /usr/local/Cellar/gcc/10.2.0_4/include/c++/10.2.0/x86_64-apple-darwin20/bits/stdc++.h` in the Terminal
