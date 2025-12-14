# bmi_calculator.py

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI with validation for extreme values"""
    if height_m <= 0:
        raise ValueError("Height must be positive")
    
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    """Determine BMI category with WHO standard ranges"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def get_positive_float(prompt, min_val=0, max_val=None):
    """Get positive float input within specified range"""
    while True:
        try:
            value = float(input(prompt))
            
            if value <= min_val:
                print(f"Please enter a number greater than {min_val}.")
                continue
                
            if max_val is not None and value > max_val:
                print(f"Please enter a number less than or equal to {max_val}.")
                continue
                
            return value
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("=== BMI Calculator ===")
    print("Note: Height should be in meters (e.g., 1.75 for 175cm)")
    
    while True:
        try:
            # Get weight with realistic limits (1-300 kg)
            weight = get_positive_float("Enter your weight in kg (1-300): ", 
                                       min_val=1, max_val=300)
            
            # Get height with realistic limits (0.5-2.5 meters)
            height = get_positive_float("Enter your height in meters (e.g., 1.75): ", 
                                       min_val=0.5, max_val=2.5)
            
            # Calculate BMI
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            
            # Display results
            print("\n" + "="*40)
            print(f"Weight: {weight:.1f} kg")
            print(f"Height: {height:.2f} m")
            print(f"BMI: {bmi:.2f}")
            print(f"Category: {category}")
            print("="*40)
            
            # Display additional health information
            print("\nBMI Categories:")
            print("• Underweight: < 18.5")
            print("• Normal weight: 18.5–24.9")
            print("• Overweight: 25–29.9")
            print("• Obesity: ≥ 30")
            
            # Ask if user wants to continue
            while True:
                again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
                if again in ['yes', 'y', 'no', 'n']:
                    break
                print("Please enter 'yes' or 'no'")
            
            if again in ['no', 'n']:
                print("\nThank you for using the BMI Calculator!")
                break
                
            print()  # Empty line for next calculation
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()