# Student Dashboard

A student academic dashboard built using Python and Streamlit to display semester-wise CGPA and overall academic performance.

## Project Overview

This project provides a simple dashboard to view student academic information, semester-wise CGPA, and first-year overall CGPA.

## Student Details

- Student Name: Preeti
- 1st Semester CGPA: 8.6
- 2nd Semester CGPA: 8.1
- Overall 1st Year CGPA: 8.35

## Features

- Student overview dashboard
- Semester-wise CGPA cards
- Automatic overall CGPA calculation
- CGPA performance bar chart
- Academic performance page
- Student information page
- Sidebar navigation

## Technologies Used

- Python
- Streamlit
- Pandas

## CGPA Calculation

Overall CGPA is calculated by taking the average of the two semester CGPAs, assuming equal semester credits.

(8.6 + 8.1) / 2 = 8.35

## How to Run

1. Clone this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:

   ```bash
   streamlit run app.py
   ```

## Project Purpose

This project was created to practice Python programming, dashboard creation, data visualization, and interactive application development.
