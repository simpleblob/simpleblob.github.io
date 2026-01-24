---

title: Project Summary - Nand2Tetris
subtitle: projected-base building a computing system from scratch
description: None
tags: computing, hardware
created: 2017-12-04
published: 2017-12-16
status: draft
confidence: log
importance: 1
---
## Link of interest

-   [nand2tetris.org](http://www.nand2tetris.org)

## Introduction

-   we are learning 3 things:
    1.  how computers work,
    2.  how to break complex problems into manageable modules,
    3.  how to develop large-scale hardware and software systems.
-   how codes work:
    1.  write C sourcecode in file
    2.  file is compiled into machine-level codes
    3.  machine-level codes (binary code-map) are executed by a chipset
        -- register, memory, ALU.
    4.  all the hardware stuff in 3. \>\> they are all logic-gates.
-   abstractions - we use it to \"split off\" complex projects into
    simple parts, as we did here.

## Lesson 01: Boolean and Logic Gates

-   Basic boolean building blocks are NOT & AND
    -   OR(X,Y) can be construct with NOT(AND(X,Y))
-   we can further discard NOT & AND by just using [NAND
    Logic](https://docs.google.com/spreadsheets/d/1vtnEP28OuOuxE_SNyYei37tIicGpcogD1NU_nhP-hw4/edit#gid=0):
    -   NOT X = NAND(X,X)
    -   X OR Y = NAND(NAND(X,X),NAND(Y,Y))
    -   X AND Y = NAND(NAND(X,Y),NAND(X,Y))
    -   Trivia: NOR can do these too. we call them \"universal gates\"
-   With these we can build up complex functions
-   For logic gates, we start with truth table work backwards to
    construct functions that can implement addition and multiplication
    etc.
-   We start with having an input of 1-bit. However, later on we will
    have more bit (16-bits etc.) to manipulate. It is better to thing of
    them as one group -- \"bus\" (latin for \"many\")
-   Building up from NANDs, the basic blocks are
    NOT,AND,OR,XOR,MUX,DMUX. (can be many-bits version).
-   Mux and Demux is useful when shared communication over a single
    line. (selecting by feeding certain frequencies to the \"select\"
    channel of Mux/Demux)
-   We can do 3-way or more combining inputs by cumulatively applying
    the basic blocks. for DMUX, it\'s similar to branching out and vice
    versa for MUX.

## Lesson 02: Boolean Arithmetic and ALU

-   How to convert from decimal to binary
    -   find the biggest \"buckets\" that decimal number can fit then
        down to the next biggest one.
    -   Example, 99 is 64 + 32 + 0 + 0 + 0 + 2 + 1
    -   Therefore, in binary form, it is 1100011
-   The following are the basic arithmetics we want to have: Add,
    Subtract, which is greater, Multiply, Divide
-   First we will get \"Add\", then we get \"Subtract\" and \"which is
    greater\" for free
    -   \"Subtract\" is adding another negative number together (this
        depends on how to represent negative numbers in a clever way)
    -   \"Greater\" means we can subtract the two numbers and see
        whether result is positive.
-   How to build Multi-bits Adder
    1.  Build Half-Adder --\> input a,b and output a sum and carry
        (called H-carry)
    2.  Build Full-Adder --\> input a,b,H-carry then output \"true sum\"
        and \"true carry\"
    3.  Build multi-bits Adder by stacking the Full-Adder cumulatively
        -- digits by digits
-   About \"ALU\" inside a cpu
    -   generally used to compute integer and logic stuff. other
        computation can be implemented later in software.
    -   in \"Hack ALU\" design, there are 2 16-bit inputs, 1 function
        select, and 1 16-bit output

## Lesson 03: Memory

-   Why do we need memory?
    -   for loop, memory \"states\", counters
    -   deal with physical speed - the gap in one discrete \"clock\"
        cycle to make sure all electrical/transistor input/output
        changes are done before one ticks.
-   Types of logic
    -   combinatorial: out\[t\] = func(in\[t\])
    -   sequential: out\[t+1\] = func(in\[t\])
-   How to implement states?
    -   in\[t+1\] = func(in\[t\]) .. AKA Flip-Flop unit (func =
        identity).
-   Register is a multi-bit register chained together
    -   WORD = width of the register
-   RAM (our actual memory unit)
    -   stores both data and code to run. remember von neumann...
    -   this is just a bunch of registers stacked together
    -   select register to manipulate by setting \"address\" and turn on
        \"load\" flag
-   Counter
    -   need this so that we could fetch the code and execute them one
        by one
    -   counter interface: RESET, NEXT, GOTO
