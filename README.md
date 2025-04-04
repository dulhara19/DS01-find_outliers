# finding outliers

## What is a Box Plot?

A box plot (also called a box-and-whisker plot) is a statistical graph used to visualize the distribution of a dataset and identify outliers. It summarizes data based on five key values:

🔹 Minimum (smallest value, excluding outliers)
🔹 First Quartile (Q1) - 25% of data is below this point
🔹 Median (Q2) - The middle value (50% of data is below, 50% above)
🔹 Third Quartile (Q3) - 75% of data is below this point
🔹 Maximum (largest value, excluding outliers)

📌 Outliers (extreme values) are plotted as individual points beyond the whiskers.

The box represents the middle 50% of data (from Q1 to Q3).

The line inside the box is the median (Q2).

The whiskers extend to the smallest and largest non-outlier values.

Outliers are plotted as separate points.

## Why Use a Box Plot?

✅ Detect outliers easily
✅ See skewness in data (if the median isn’t centered in the box)
✅ Compare distributions between different datasets

Integer Quartiles (No Interpolation)

📊 Dataset (sorted) → [5, 10, 15, 20, 25, 30, 35, 40] (n = 8)

    Q1 Position = (8+1)4=2.254(8+1)​=2.25 → 2nd value = 10

    Q3 Position = 3(8+1)4=6.7543(8+1)​=6.75 → 6th value = 30

So, Q1 = 10 and Q3 = 30. 


Float Quartiles (Interpolation Required)

📊 Dataset (sorted) → [5, 10, 15, 20, 25, 30, 35, 40, 100] (n = 9)

    Q1 Position = (9+1)4=2.54(9+1)​=2.5 → Between 2nd (10) and 3rd (15)
    Q1=10+(15−10)2=12.5
    Q1=10+2(15−10)​=12.5

    Q3 Position = 3(9+1)4=7.543(9+1)​=7.5 → Between 7th (35) and 8th (40)
    Q3=35+(40−35)2=37.5
    Q3=35+2(40−35)​=37.5