# notes.md
Random notes.

## What is it?
Lani is essentially a new programming language that can be
described as bilingual IBM HLAM and python.

## Hierarchy
Here is where `lani` exists in my mind's eye.

1. Architecture - s390x, arm, x86, etc.
2. Language - C, MIPS, HLASM, etc.
3. Operating System - Windows, z/OS, Ubuntu, etc.
4. Applications - ls, DFSORT, submit, etc.

Thus, `lani` acts as a translation layer between a computer 
architecture, such as `ARM`, and an operating system like Windows 11.

### Architecture
The `lani` language supports all modern computer architectures by
leveraging existing compilers, but it targets consumer hardware and 
the s390x (z/Architecture) platforms in particular.

### Language
I will probably implement `lani` as a CPython package, but at some
point I intend to build a custom python interpreter to remove the 
dependency on CPython. However, supporting CPython is important
because it is widely used on IBM mainframes and consumer electronics.

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
