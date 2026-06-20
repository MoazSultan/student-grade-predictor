# student-grade-predictor
Student Performance Prediction Using Bayesian Networks (Python, pgmpy) Developed an AI-based probabilistic model to predict students' final grades based on attendance, study hours, motivation, assignments, and internal assessments using Bayesian Networks and Variable Elimination
# Student Performance Prediction Using Bayesian Networks

## Abstract

This project presents a Bayesian Network–based model for predicting student academic performance. The model captures probabilistic relationships among attendance, study hours, assignments, internal assessments, and motivation to predict the final grade of a student.

---

## Introduction

Predicting student performance is an important task in educational analytics. Bayesian Networks provide a structured and probabilistic approach to model uncertainty and causal relationships among multiple academic factors.

---

## Objectives

* Identify key academic factors influencing student performance.
* Model dependencies using Bayesian Networks.
* Predict final semester grades probabilistically.
* Develop an extendable academic prediction system.

---

## Variables Used

| Variable           | Description                  | States                  |
| ------------------ | ---------------------------- | ----------------------- |
| Attendance         | Class attendance percentage  | Low, Medium, High       |
| StudyHours         | Daily study duration         | Low, Medium, High       |
| AssignmentScore    | Assignment performance       | Poor, Average, Good     |
| InternalAssessment | Quiz and midterm performance | Poor, Average, Good     |
| Motivation         | Student motivation level     | Low, Medium, High       |
| FinalGrade         | Overall semester result      | Fail, Pass, Distinction |

---

## Bayesian Network Structure

The network contains the following dependencies:

* Attendance → AssignmentScore
* Attendance → InternalAssessment
* StudyHours → Motivation
* AssignmentScore → FinalGrade
* InternalAssessment → FinalGrade
* Motivation → FinalGrade

These dependencies represent real-world relationships between academic factors and student outcomes.

---

## Conditional Probability Tables (CPTs)

### Attendance (Prior Probabilities)

| State  | Probability |
| ------ | ----------- |
| Low    | 0.30        |
| Medium | 0.40        |
| High   | 0.30        |

### Study Hours (Prior Probabilities)

| State  | Probability |
| ------ | ----------- |
| Low    | 0.35        |
| Medium | 0.40        |
| High   | 0.25        |

### Assignment Score Given Attendance

| Attendance | Poor | Average | Good |
| ---------- | ---- | ------- | ---- |
| Low        | 0.60 | 0.30    | 0.10 |
| Medium     | 0.30 | 0.45    | 0.25 |
| High       | 0.15 | 0.35    | 0.50 |

### Internal Assessment Given Attendance

| Attendance | Poor | Average | Good |
| ---------- | ---- | ------- | ---- |
| Low        | 0.55 | 0.35    | 0.10 |
| Medium     | 0.30 | 0.40    | 0.30 |
| High       | 0.15 | 0.30    | 0.55 |

### Motivation Given Study Hours

| Study Hours | Low  | Medium | High |
| ----------- | ---- | ------ | ---- |
| Low         | 0.60 | 0.30   | 0.10 |
| Medium      | 0.30 | 0.45   | 0.25 |
| High        | 0.10 | 0.30   | 0.60 |

---

## Technologies Used

* Python
* pgmpy
* Bayesian Networks
* Variable Elimination Algorithm

---

## Features

* Probabilistic prediction of student performance.
* Modeling of uncertainty using Bayesian Networks.
* Interactive user input for attendance and study hours.
* Prediction of final grades as **Fail**, **Pass**, or **Distinction**.

---

## Future Improvements

* Incorporate CGPA and previous semester records.
* Train probabilities using real-world datasets.
* Develop a graphical user interface (GUI).
* Add visualization of the Bayesian Network.

---

## Author

**Muhammad Moaz Sultan**
BS Software Engineering
