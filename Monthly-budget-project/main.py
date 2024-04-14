def main():
  # Step 1: Prompt the user to input their monthly budget limit
  budget_limit = float(input("Enter your monthly budget limit: "))

  # Step 2: Prompt the user to input their savings account balance
  savings_balance = float(input("Enter your savings account balance: "))

  # Step 3: Calculate auto-savings amount (10% of the budget limit)
  auto_savings = budget_limit * 0.10

  # Step 4: Deduct auto-savings from the budget limit
  budget_limit -= auto_savings

  # Step 5: Initialize total expenses to 0
  total_expenses = 0

  # Step 6: Loop through each expense category
  expense_categories = ["Rent", "Utilities", "Groceries", "Transportation", "Entertainment"]
  for category in expense_categories:
      # Step 6.1: Prompt the user to input the amount spent on the current expense category
      expense = float(input(f"Enter amount spent on {category}: "))
      # Step 6.2: Add the amount spent to total expenses
      total_expenses += expense

  # Step 7: Calculate the difference between the budget limit (after auto-savings) and total expenses
  difference = budget_limit - total_expenses

  # Step 8: Check if total expenses (including auto-savings) are within the adjusted budget limit
  if total_expenses <= budget_limit:
      # Step 8.1: If within budget, display appropriate message
      print("You are within your budget.")
  else:
      # Step 8.2: If expenses exceed adjusted budget, calculate by how much and display message
      excess = total_expenses - budget_limit
      print(f"You have exceeded your budget by {excess}.")

  # Step 9: Display the total expenses incurred (including auto-savings) and the auto-savings amount
  print("Total expenses incurred (including auto-savings):", total_expenses)
  print("Auto-savings amount:", auto_savings)

if __name__ == "__main__":
  main()

