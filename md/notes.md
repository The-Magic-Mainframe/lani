# notes.md
Random notes.

## What is it?
Lani is essentially a new programming language that can be
described as bilingual IBM HLASM and python.

## Hierarchy
Here is where `lani` exists in my mind's eye.

1. Architecture - s390x, arm, x86, etc.
2. Language - C, MIPS, HLASM, `lani`, etc.
3. Operating System - Windows, z/OS, Ubuntu, etc.
4. Applications - ls, DFSORT, submit, etc.

Thus, `lani` acts as a translation layer between a computer 
architecture, such as `ARM`, and an operating system like Windows 11.

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
* `lani-os` - The lani virtual operating system.
  * Dispatcher
    * Allocation
    * Scheduling
  * Storage Manager
    * Real
    * Virtual
    * File System
    * Backup
  * I/O and Device Manager
  * Communication Protocols and Servers
* `lani-util` - Tools for the 
  * `IEFBR142` - Just another "do nothing" program
  * `fuller` - A [fuller](https://github.com/The-Magic-Mainframe/fuller) SPOOL archiver.
  * `submit` - Submit jobs to batch processing subsystem.
