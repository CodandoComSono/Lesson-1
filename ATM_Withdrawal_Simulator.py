print("=== ATM WITHDRAWAL SIMULATOR ===")

value = int(input("Enter the amount to withdraw: $ "))

remaining = value

bills50 = remaining // 50
remaining %= 50

bills20 = remaining // 20
remaining %= 20

bills10 = remaining // 10
remaining %= 10

bills1 = remaining // 1

print("\n=== BILLS DISPENSED ===")
print(f"$50: {bills50}")
print(f"$20: {bills20}")
print(f"$10: {bills10}")
print(f"$1:  {bills1}")
print("\nOperation completed.")

ATM_Withdrawal_Simulator.py
Program that simulates an ATM withdrawal and shows the number of bills needed.