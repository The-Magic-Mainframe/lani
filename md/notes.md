# notes.md
Random notes.

## What is it?
There are a number of pieces, but I consider `lani` itself to be a 
programming language. I intend to use this programming language to 
implement something like the Windows Subsystem For Linux (WSL). The 
difference between `lani` and WSL is that `lani` is cross-platform 
and implement something like z/OS rather than linux.

## Hierarchy
Some layers to think about.

1. Architecture - s390x, arm, x86, etc.
2. Language - C, MIPS, HLASM, `lani`, etc.
3. Operating System - Windows, z/OS, Ubuntu, etc.
4. Applications - ls, DFSORT, submit, etc.

Thus, `lani` acts as a translation layer between a computer 
architecture, such as `ARM`, and an operating system like Windows 11.
It also allows a programmer to create and deploy cross-platform
applications in a mixed computing environment.

### Architecture
The `lani` language supports all modern computer architectures by
leveraging existing compilers, but it targets consumer hardware and 
the s390x (z/Architecture) platforms in particular. When not running on s390x, the `lani` interpreter emulates s390x hardware features.

### Language
I will probably implement `lani` as a CPython package at this time, this the language is technically a subset of the Python language.

Eventually, I would like to remove this dependency on the cpython interpreter and language. But this is where I will be starting.

### Operating System
Using the `lani` language, I intend to implement a mediation layer
similar to the _Windows Subsystem for Linux_ (WSL). The intent will
be to create an operating system within an operating system with
full support for applications written for IBM Z operating systems.

### Applications
I intend to implement or in some cases re-implement some UNIX-like
utilities for IBM Z operating systems. These will run as native
applications on the host machine, firing up the pieces of the 
operating system mediation layer as needed.

## Implementation
* `lani` - Bilingual HLASM / python implemented in C.
  * Variables/Symbols
    * Data structures
    * Data types
    * Data representation
    * Data manipulation
  * Instructions
    * Assembly
      * AMODE, RSECT, DS, DC, ORG, etc...
    * Runtime
      * General, Control, Math, Vector, I/O
    * S/360, S/370, ESA, z/Architecture
* `lani-vm` - The lani virtual machine.
    * CPU
      * 1 or more
      * Spawned as processes
    * Registers
      * General, Control, AR, Floating
      * PSW, PSWE, ...
      * TOD, BEAR, etc...
    * Cache
      * L1, L2, L3
    * Core storage
    * Facility emulation
    * Device emulation
* `lani-vos` - The lani virtual operating system.
  * Dispatcher
    * Allocation
    * Scheduling
  * Storage Manager
    * Virtual
    * File System
    * Backup
  * I/O and Device Manager
  * Communication Protocols and Servers
* `lani-vutil` - Tools for the lani virtual operating system.
  * `IEFBR142` - Just another "do nothing" program
  * `fuller` - A [fuller](https://github.com/The-Magic-Mainframe/fuller) SPOOL archiver.
  * `submit` - Submit jobs to batch processing subsystem.

## Packages
* `lani`
  * `lani.Memory`
    * `lani.Instruction`

* `lani.vm`
  * `lani.vm.Machine`
  * `lani.vm.Register`
    * `lani.vm.GeneralRegister`
    * `lani.vm.ControlRegister`
    * `lani.vm.PSWE`
* `lani.vos`
* `lani.vutil`
  * `lani.vutil.fuller`
  * `lani.vutil.iefbr142`
  * `lani.vutil.submit`
  * [Z Open Automation Utilities](https://www.ibm.com/docs/en/zoau/1.2.x?topic=zoau-functionality-overview)
