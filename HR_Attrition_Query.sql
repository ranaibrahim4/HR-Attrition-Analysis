-- HR Attrition Analysis
-- Summary by Department and Job Role

SELECT
    d.DepartmentName,
    j.JobRoleName,

    SUM(
        CASE
            WHEN e.Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS AttritionCount,

    ROUND(
        AVG(e.MonthlyIncome),
        2
    ) AS AverageMonthlyIncome

FROM FactEmployee AS e

LEFT JOIN DimDepartment AS d
    ON e.DepartmentKey = d.DepartmentKey

LEFT JOIN DimJobRole AS j
    ON e.JobRoleKey = j.JobRoleKey

GROUP BY
    d.DepartmentName,
    j.JobRoleName

ORDER BY
    AttritionCount DESC;