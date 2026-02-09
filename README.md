# FUENTES-Lara-Rain-B.
I explored how decimal precision affects scientific math by testing pi up to 100 places. Using the Pendulum Period formula, I compared Truncation vs. Rounding to see which method minimizes error. This shows pi as a fundamental constant of time and gravity, not just circles.

<img width="1490" height="858" alt="Screenshot 2026-02-09 091734" src="https://github.com/user-attachments/assets/128d781d-6dca-4c6e-973b-2698977f48e4" />
<img width="1176" height="385" alt="Screenshot 2026-02-09 091807" src="https://github.com/user-attachments/assets/bf7bb752-b51f-473a-ae07-7498ae4fab0e" />

For the Terminal Table (The Grid of Numbers)
This table compares Truncation and Rounding side-by-side. By using a '+1 peek digit,' you can see exactly where the two methods diverge. The 'YES' markers at 40 and 60 digits prove that rounding the input of pi leads to a more precise calculation of the pendulum's period.

For the Initial Green Graph (The Flat Line)
This graph shows the overall stability of the Pendulum Period formula. It demonstrates that while we are increasing the precision of pi on the X-axis, the physical result remains constant at approximately 2.006 seconds, proving the formula is reliable for real-world applications.

For the Red and Green Error Graphs (The Sloping Lines)
Since the differences in precision are too small to see on a standard scale, I used a Logarithmic Error Graph to visualize the 'residual error.' The steep downward slope represents the exponential increase in accuracy as more decimals are added. Comparing the two lines confirms that the Rounding method (green) consistently maintains a lower error margin than simple Truncation (red).

