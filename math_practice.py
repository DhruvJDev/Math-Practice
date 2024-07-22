import random

def generate_number_a():
  """Generates two random two-digit numbers."""
  num1 = random.randint(10, 999)
  num2 = random.randint(10, 99)
  return num1, num2

# Addition
def add():
  """Generates and adds two random two-digit numbers, checks user's answer in a loop."""
  while True:
    num1, num2 = generate_number_a()
    add_expected = num1 + num2

    print(f"\nWhat is the sum of \n  {num1}\n+  {num2}")

    # Get user's answer
    while True:
      try:
        user_add = int(input("Enter your answer: "))
        break
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Check if the answer is correct
    if user_add == add_expected:
      # print("Correct! The answer is", add_expected)
      print("✔ Correct")
    else:
      # print("Incorrect. The sum is", add_expected, ", but you entered", user_add)
      print("✘ Incorrect. The sum of", num1,"+", num2,"=", add_expected)



def generate_number_s():
  """Generates two random two-digit numbers."""
  num1 = random.randint(10, 99)
  num2 = random.randint(10, 99)
  return num1, num2
# Subtraction
def sub():
  """Generates and adds two random two-digit numbers, checks user's answer in a loop."""
  while True:
    num1, num2 = generate_number_s()
    sub_expected = num1 - num2

    print(f"\nWhat is the subtraction of \n  {num1}\n- {num2}")

    # Get user's answer
    while True:
      try:
        user_sub = int(input("Enter your answer: "))
        break
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Check if the answer is correct
    if user_sub == sub_expected:
    #   print("Correct! The answer is", sub_expected)
      print("Correct!")
    else:
    #   print("Incorrect. The sum is", sub_expected, ", but you entered", user_sub)
      print("✘ Incorrect. The subtraction of", num1,"-", num2,"=", sub_expected)

def generate_number_m():
  """Generates two random two-digit numbers."""
  num1 = random.randint(2, 9)
  num2 = random.randint(2, 9)
  return num1, num2





# Multiplication
def mul():
  """Generates and adds two random two-digit numbers, checks user's answer in a loop."""
  while True:
    num1, num2 = generate_number_m()
    mul_expected = num1 * num2

    print(f"\nWhat is the multiplication of \n  {num1}\nX {num2}")

    # Get user's answer
    while True:
      try:
        user_mul = int(input("Enter your answer: "))
        break
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Check if the answer is correct
    if user_mul == mul_expected:
    #   print("Correct! The answer is", sub_expected)
      print("✔ Correct")
    else:
    #   print("Incorrect. The sum is", sub_expected, ", but you entered", user_sub)
      print("✘ Incorrect. The multiplication of", num1,"X", num2,"=", mul_expected)

def generate_number_d():
  """Generates two random two-digit numbers."""
  num1 = random.randint(2, 9)
  num2 = random.randint(2, 9)
  return num1, num2





# Divadation


# def div():
  """Generates and adds two random two-digit numbers, checks user's answer in a loop."""
  while True:
    num1, num2 = generate_number_d()
    div_expected = num1 / num2

    print(f"\nWhat is the divadation of \n  {num1}\n÷ {num2}")

    # Get user's answer
    while True:
      try:
        user_div = float(input("Enter your answer: "))
        break
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Check if the answer is correct
    if user_div == div_expected:
    #   print("Correct! The answer is", sub_expected)
      print("✔ Correct")
    else:
    #   print("Incorrect. The sum is", sub_expected, ", but you entered", user_sub)
      print("✘ Incorrect. The divadation of", num1,"÷", num2,"=", mul_expected)




def div():
  """Generates and adds two random two-digit numbers, checks user's answer in a loop."""
  while True:
    num1, num2 = generate_number_d()
    div_expected = num1 / num2

    print(f"\nWhat is the divadation of \n  {num1}\n÷ {num2}")

    # Get user's answer
    while True:
      try:
        user_div = float(input("Enter your answer: "))
        break
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Check if the answer is correct (within 0.005 tolerance)
    epsilon = 0.005  # Adjust epsilon for desired precision
    if abs(user_div - div_expected) < epsilon:
      print("✔ Correct")
    else:
      # Format both results to show only 2 decimal places
      formatted_user_div = f"{user_div:.2f}"
      formatted_expected = f"{div_expected:.2f}"
      print(f"Incorrect. The divadation of {num1} ÷ {num2} = {formatted_expected}")




# Main
def main():
  """Provides a menu-driven interface for math operations."""

  while True:
    print("\nMath Operations Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division (Integer)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      if __name__ == "__main__":
        add()

    elif choice == '2':
      if __name__ == "__main__":
        sub()
    elif choice == '3':
      if __name__ == "__main__":
        mul()
    elif choice == '4':
      if __name__ == "__main__":
        div()
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")
      continue
if __name__ == "__main__":
    main()
