# Blinky [![License](https://img.shields.io/github/license/IMBeniamin/Blinky.svg)](https://github.com/IMBeniamin/Blinky/blob/main/LICENSE)
[![Discord](https://img.shields.io/badge/RxCord%20Server--blue.svg?style=social&logo=Discord)](https://discord.gg/yv4VnZT)

Blinky is a game engine project in its very early stages of development with a focus towards learning.
There is currently no clear roadmap, however most basic functionality should be implemented to the point where game developing is possible.

***

## Starting out
Visual Studio version 2019 or newer is recommended and all other development enviroments are untested. It is however worth noting that a project setup toolchain using premake is developed and available for use, which allows the use of many different build systems.
For a comprehensive list of available build systems please check the [premake documentation](https://premake.github.io/docs/Using-Premake).

#### <ins>**1. Cloning the repository:**</ins>

To clone the repository using git run the following command in a git supported terminal:
`git clone --recursive https://github.com/IMBeniamin/Blinky.git`

The command clones the repository recursively, which means that all submodules and dependencies are also clone.

If for some reason the repository was not cloned recursively, running the file [init.bat](https://github.com/IMBeniamin/Blinky/blob/main/scripts/Windows/init.bat) will fix the repository by cloning all dependencies. This can be also done manually by running the command `git submodule update --init --recursive` in a git supported terminal.

#### <ins>**2. Configuring the dependencies:**</ins>
- #### Windows
  1. Run the [init.bat](https://github.com/IMBeniamin/Blinky/blob/main/scripts/Windows/init.bat) file found in the `scripts` folder and follow all instructions given. This file will trigger a setup python script that will download the all prerequisites for the project if they are not present and install them.
        *<span style="color:darkgray">If you do not want to use the `.bat` you can also run the python script directly from a supported terminal. The python version is always automatically checked to ensure compatibility at runtime.</span>*

- #### OS X
  - Work in progress.

- #### Linux
  - Work in progress.

If changes are made, or if you want to regenerate the project files you can do so by rerunning the [init.bat](https://github.com/IMBeniamin/Blinky/blob/main/scripts/Windows/init.bat) file.

***

## Objectives
- Implement basic systems like the renderer, an audio engine, an entity system, etc
- Provide good documentation in order to facilitate learning
- Stay up to date with current technologies as to experiment with them and have a hands-on experience
