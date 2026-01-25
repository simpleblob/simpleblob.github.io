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

This course teaches three things:

1. How computers work
2. How to break complex problems into manageable modules
3. How to develop large-scale hardware and software systems

### How Code Works

1. Write C source code in a file
2. File is compiled into machine-level code
3. Machine-level code (binary) is executed by a chipset: register, memory, ALU
4. All the hardware in step 3 is built from logic gates

**Abstractions** let us split complex projects into simple parts.

## Lesson 01: Boolean and Logic Gates

### Basic Building Blocks

The basic boolean building blocks are NOT and AND. We can construct OR(X,Y) using NOT(AND(X,Y)).

### NAND Logic: The Universal Gate

We can build everything using just [NAND gates](https://docs.google.com/spreadsheets/d/1vtnEP28OuOuxE_SNyYei37tIicGpcogD1NU_nhP-hw4/edit#gid=0):

- NOT X = NAND(X,X)
- X OR Y = NAND(NAND(X,X),NAND(Y,Y))
- X AND Y = NAND(NAND(X,Y),NAND(X,Y))

NOR gates can also do this. We call them "universal gates."

### Building Complex Functions

With these gates we can build complex functions. For logic gates, we start with a truth table and work backwards to construct functions that implement addition, multiplication, etc.

### Buses: Groups of Bits

We start with 1-bit inputs. Later we manipulate 16-bits or more. Think of them as one group called a "bus" (Latin for "many").

### Core Components

Building up from NANDs, the basic blocks are NOT, AND, OR, XOR, MUX, DMUX. These can all have multi-bit versions.

**MUX and DMUX** are useful for shared communication over a single line. Select signals control which input or output is active.

We can create 3-way or more inputs by cumulatively applying the basic blocks. DMUX branches out. MUX combines back together.

## Lesson 02: Boolean Arithmetic and ALU

### Decimal to Binary Conversion

Find the biggest "buckets" that a decimal number can fit, then work down to the next biggest.

**Example:** 99 = 64 + 32 + 0 + 0 + 0 + 2 + 1

In binary form: 1100011

### Basic Arithmetic Operations

We want these operations: Add, Subtract, Greater Than, Multiply, Divide.

First we build Add. Then we get Subtract and Greater Than for free:

- **Subtract** is adding a negative number (depends on clever representation of negative numbers)
- **Greater Than** means we subtract two numbers and check if the result is positive

### Building a Multi-Bit Adder

1. Build Half-Adder: input a, b and output sum and carry (H-carry)
2. Build Full-Adder: input a, b, H-carry and output true sum and true carry
3. Build multi-bit Adder by stacking Full-Adders cumulatively, digit by digit

### The ALU (Arithmetic Logic Unit)

The ALU computes integer and logic operations. Other computation can be implemented later in software.

In the Hack ALU design: 2 16-bit inputs, 1 function select, and 1 16-bit output.

## Lesson 03: Memory

### Why We Need Memory

- For loops, memory states, and counters
- To handle physical speed: the gap in one discrete clock cycle ensures all electrical and transistor changes complete before the next tick

### Types of Logic

**Combinatorial:** out[t] = func(in[t])

**Sequential:** out[t+1] = func(in[t])

### Implementing State

State is implemented as in[t+1] = func(in[t]). This is the Flip-Flop unit (where func = identity).

### Register

A register is multiple bits chained together. The WORD is the width of the register.

### RAM (Random Access Memory)

RAM stores both data and code to run. Remember von Neumann architecture.

RAM is just a bunch of registers stacked together. Select which register to manipulate by setting the address and turning on the load flag.

### Counter

We need a counter to fetch code and execute instructions one by one.

Counter interface: RESET, NEXT, GOTO.
