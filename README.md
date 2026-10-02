# AI-LAB-02
# Artificial Intelligence - Lab 02: Python Iterative Structures, Functions & OOP

This repository contains the practical implementation and source code exercises for **Lab 02** of the **Artificial Intelligence** course. The focus of this lab is on mastering core programming constructs in Python essential for AI algorithms: control loops, functional modularity, and object-oriented programming (OOP).

---

## 📑 Table of Contents

- [Overview](#overview)
- [Topics Covered](#topics-covered)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [File Descriptions & Concepts](#file-descriptions--concepts)
  - [1. For Loops](#1-for-loops-01_for_loopspy)
  - [2. While Loops](#2-while-loops-02_while_loopspy)
  - [3. Loop Control Statements](#3-loop-control-statements-03_loop_breakpy--04_loop_continuepy)
  - [4. Functions](#4-functions-05_functions_overviewpy)
  - [5. Classes and Objects](#5-classes-and-objects-06_classes_and_objectspy)
- [Author](#author)

---

## 🎯 Overview

Python is the standard language for Artificial Intelligence and Machine Learning implementations. This lab explores fundamental building blocks required for state-space searches, iterative updates, agent definitions, and object-oriented problem-solving.

---

## 📚 Topics Covered

1. **Iterative Structures (`for`, `while`):**
   - Sequential traversal over collections (`list`, `tuple`, `str`).
   - Range- and index-based iteration (`range(len(...))`).
   - Conditional termination with `while` loops and single-statement loops.
2. **Loop Flow Controls:**
   - Terminating execution using `break`.
   - Skipping steps using `continue`.
3. **Modular Programming with Functions:**
   - Parameter passing, default values, and keyword arguments (`kwargs`).
   - Handling data structures (lists) inside functions.
   - Return values.
4. **Object-Oriented Programming (OOP):**
   - Class blueprints and instance creation.
   - Initializer constructor (`__init__`) and state handling (`self`).
   - Encapsulation of instance methods.

---

## 📂 Repository Structure

```plaintext
.
├── 01_for_loops.py              # Sequence traversal (List, Tuple, String, Indexing)
├── 02_while_loops.py            # Standard & inline while loop syntax
├── 03_loop_break.py             # Early termination with break
├── 04_loop_continue.py          # Skipping iterations with continue
├── 05_functions_overview.py     # Parameters, default values, keyword args & returns
├── 06_classes_and_objects.py    # Class definitions, constructors, and methods
├── Lab 2.pdf                    # Lab instructions and theoretical background
└── README.md                    # Project documentation
```

---

## ⚙️ Prerequisites

- Python 3.8 or above installed on your machine.
- Terminal, Command Prompt, or an IDE (such as VS Code, PyCharm, or Jupyter).

Check your installation:
```bash
python --version
# or
python3 --version
```

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Run any script directly using Python:**
   ```bash
   python 01_for_loops.py
   python 02_while_loops.py
   python 03_loop_break.py
   python 04_loop_continue.py
   python 05_functions_overview.py
   python 06_classes_and_objects.py
   ```

---

## 🔍 File Descriptions & Concepts

### 1. For Loops (`01_for_loops.py`)
Demonstrates how Python executes sequential iteration over iterable data structures:
- Traversing `list` and `tuple` containers.
- Iterating through characters in a `str`.
- Accessing elements via position index with `range(len(...))`.

### 2. While Loops (`02_while_loops.py`)
Explores condition-driven iteration:
- Multi-line block loops checking termination conditions each cycle.
- Single-statement/one-liner `while` blocks.

### 3. Loop Control Statements (`03_loop_break.py` & `04_loop_continue.py`)
Alters loop execution dynamically:
- **`break`**: Immediately terminates loop flow upon encountering matching conditions.
- **`continue`**: Skips the remaining body of the current iteration and jumps to the next cycle.

### 4. Functions (`05_functions_overview.py`)
Covers code reusability and functional design:
- Defining and calling standard functions (`def`).
- Positional vs. keyword arguments.
- Default parameter values (fallback parameters).
- Passing data structures (lists) into functions and computing return values.

### 5. Classes and Objects (`06_classes_and_objects.py`)
Demonstrates basic Object-Oriented design:
- Instantiating classes and referencing attributes.
- Defining constructors with `__init__(self, ...)` to bind instance state.
- Defining member methods that interact with object properties.

---

## 👤 Author

- **Name:** Ahmad Abdullah Ejaz
- **Course:** Artificial Intelligence 
