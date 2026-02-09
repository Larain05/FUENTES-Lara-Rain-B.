import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP

#I use Pendulum Period (T = 2π * sqrt(L/g)) as a test case because it is a well-known formula that depends directly on π, and small changes in π can lead to noticeable differences in the calculated period. 
#This makes it an ideal example to demonstrate the effects of truncation and rounding on precision.        

#110 digits of internal precision
getcontext().prec = 110

#Physics Constants
PI_CONSTANT = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
G = Decimal('9.80665') #Gravity
L = Decimal('1.0') #1 meter Pendulum Length

def pendulum_period(pi_val):
    #T= 2 * pi * sqrt(L / g)
    return Decimal(2) * pi_val * (L / G).sqrt()

true_period = pendulum_period(PI_CONSTANT)
levels = [20, 40, 60, 100]
trunc_errors, round_errors = [], []

print("=" * 120)
print(f"{'DIGITS':<8} | {'METHOD':<12} | {'CALCULATED PERIOD T (with +1 peek digit)':<80} | {'CLOSER?'}")
print("=" * 120)

for p in levels:
    #Prepare Pi versions
    pi_t = PI_CONSTANT.quantize(Decimal('1.' + '0'*p), rounding=ROUND_DOWN)
    pi_r = PI_CONSTANT.quantize(Decimal('1.' + '0'*p), rounding=ROUND_HALF_UP)
    
    #Calculate Results
    t_t = pendulum_period(pi_t)
    t_r = pendulum_period(pi_r)
    
    #Calculate Errors for Plotting
    err_t, err_r = abs(true_period - t_t), abs(true_period - t_r)
    trunc_errors.append(float(err_t))
    round_errors.append(float(err_r))
    
    closer_r = "YES" if err_r < err_t else "No (Equal)"
    
    #Format Terminal Output (Slicing to p+3 to show the peek digit)
    #The +3 accounts for the "2." and the extra digit at the end
    print(f"{p:<8} | Truncation | {str(t_t)[:p+3]:<80} | ---")
    print(f"{'':<8} | Rounding   | {str(t_r)[:p+3]:<80} | {closer_r}")
    print("-" * 120)

#VISUALIZATION
plt.figure(figsize=(12, 7))
plt.plot(levels, trunc_errors, marker='o', label='Truncation Error', color='red', linewidth=2)
plt.plot(levels, round_errors, marker='s', label='Rounding Error', color='green', linestyle='--', linewidth=2)

plt.yscale('log') #Log scale is vital to see the tiny differences
plt.title('Precision Error Comparison: Truncation vs. Rounding', fontsize=14)
plt.xlabel('Number of Decimals of Pi Used', fontsize=12)
plt.ylabel('Error (Distance from True Value)', fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()