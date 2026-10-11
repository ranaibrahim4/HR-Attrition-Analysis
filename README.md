# HR Attrition Analysis

## Project Overview

This project analyzes synthetic employee attrition data using Power BI, DAX, SQL, SQLite, and Python.

The project aims to:

- Measure overall employee attrition.
- Identify departments and job roles with higher attrition.
- Examine factors associated with employees leaving.
- Classify employees by experience level.
- Recommend potential employee-retention actions.

> **Data disclaimer:** This project uses a completely synthetic dataset created for assessment, learning, and portfolio purposes. It does not contain information about real employees or organizations.

---

## Tools and Technologies

- Power BI
- DAX
- SQL
- SQLite
- Python
- Visual Studio Code
- Microsoft Excel

---

## Dataset

The synthetic dataset contains **600 fictional employee records**.

Important fields include:

- Department
- Job Role
- Age
- Monthly Income
- Overtime
- Business Travel
- Job Satisfaction
- Environment Satisfaction
- Total Working Years
- Years at Company
- Attrition

### Main workforce figures

- **Total employees:** 600
- **Employees who left:** 154
- **Active employees:** 446
- **Overall attrition rate:** 25.7%
- **Average total working years:** 13.4

---

## Data Model

The Power BI report uses a star-schema structure with:

- `FactEmployee`
- `DimDepartment`
- `DimJobRole`

The relationships are:

- `DimDepartment[DepartmentKey]` to `FactEmployee[DepartmentKey]`
- `DimJobRole[JobRoleKey]` to `FactEmployee[JobRoleKey]`

Both relationships use one-to-many cardinality and single-direction filtering.

images/Data_Model.png

---

## Power BI Dashboard

### Employee Attrition Overview

The Executive Overview presents the main workforce KPIs and compares attrition across departments and job roles.

images/Executive_Overview.png

### Attrition Drivers and Risk Factors

The second page examines factors associated with higher employee attrition, including overtime, business travel, job satisfaction, experience level, and monthly income.

images/Drivers_Risk_Factors.png

---

## DAX Measures

The Power BI report includes DAX measures created using variables.

The main measures are:

- Total Employees
- Attrition Count
- Active Employees
- Attrition Rate
- Average Monthly Income
- Average Working Years
- Maximum Monthly Income
- Minimum Monthly Income


    Rate
