# 🧩 Data Munging (OOP + SOLID Principles)

## 📘 Overview
This project is based on the [CodeKata #04 - Data Munging](http://codekata.com/kata/kata04-data-munging) problem.  
It demonstrates how to apply **Object-Oriented Programming (OOP)** and **SOLID principles** to refactor procedural code into a clean, modular design.

The goal is to extract, analyze, and calculate data differences from text files (like weather and soccer datasets) using reusable components.

---

## 🎯 Objectives
- Parse raw data files (e.g., `weather.dat`, `football.dat`)
- Find the row with the smallest difference between two columns
- Apply **OOP** concepts such as:
  - Encapsulation  
  - Abstraction  
  - Reusability  
- Apply **SOLID** design principles to keep code maintainable and extensible.

---


---

## 🧱 Class Responsibilities

### 🧮 `Calculator`
- Acts as the controller.
- Initializes `DataExtractor` and `DataAnalyzer`.
- Executes the process from data loading → analysis → result.

### 📂 `DataExtractor`
- Responsible **only** for reading data.
- Extracts specific columns as per user input.
- Keeps file handling separate from logic.

### 📊 `DataAnalyzer`
- Responsible for performing data operations.
- Finds the record with **minimum difference** between two numeric columns.

---






