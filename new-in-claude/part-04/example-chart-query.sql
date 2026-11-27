-- Example output, written for the made-up sales table above; not run, and not Claude's own output.
-- Each Claude Data chart shows its own query: open it to check what the chart is counting.
SELECT month, item, SUM(units_sold)
FROM sales
WHERE month IN ('2026-10', '2026-11')
GROUP BY month, item
