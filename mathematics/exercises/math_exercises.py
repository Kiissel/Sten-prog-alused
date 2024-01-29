"""Math exercises."""
import math

def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    sum = num_a / num_b
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    num = num_a // num_b
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = (num_a + num_b)/2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    circle_area = round(math.pi *(radius**2), 2)
    return circle_area


def area_of_an_equilateral_triangle(side_length: float) -> float:
    """Calculate and return the area of an equilateral triangle."""
    # Formula for the area of an equilateral triangle
    triangle_area = round((math.sqrt(3) * side_length ** 2) / 4)
    return area


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Formula for the discriminant
    discriminant = b**2 - 4*a*c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of the hypotenuse when the lengths of the catheti are given."""
    # Formula for calculating the hypotenuse in a right-angled triangle
    c = math.sqrt(a**2 + b**2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Formula for calculating one cathetus in a right-angled triangle
    b = math.sqrt(c**2 - a**2)
    return b


def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    # Convert seconds to hours and minutes
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} seconds is {hours} hour(s) and {minutes} minute(s)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    # Convert angle to radians for trigonometric functions
    angle_rad = math.radians(angle)
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    return f"Angle: {angle}, sine: {sine}, cosine: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey " * n
    return lots_of_heys.strip()


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a + num_b)
    return string_numbers
