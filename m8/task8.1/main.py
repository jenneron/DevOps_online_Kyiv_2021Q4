
def main():
    print("Enter a: ", end="")
    a = input()
    a = validate_param(a, is_a=True)

    print("Enter b: ", end="")
    b = input()
    b = validate_param(b)

    print("Enter c: ", end="")
    c = input()
    c = validate_param(c)

    square_print(
        int(a), int(b), int(c),  # a, b, c
        solv_square(int(a), int(b), int(c))  # roots array
        )


def validate_param(var, is_a=False, tries=3):
    """
    Validate that parameter string is convertable to int. If no, 
    then give 2 more tries to input. Return converted value.
    
    Also validate that a != 0.
    """
    if tries == 0:
        print("ERROR: 3 tries are exceeded, exiting")
        exit()

    # Get new input
    if tries < 3:
        print("Enter again: ", end="")
        var = input()

    new_try = lambda: validate_param(
            var,  # value
            is_a=is_a,  # pass this argument again
            tries=(tries - 1)  # one less try left
            )

    try:
        result = int(var)
    except ValueError:
        print("ERROR: The input must be integer")
        return new_try()

    if is_a and result == 0:
        print("ERROR: a must not be 0")
        return new_try()

    return result


def discriminant(a, b, c):
    print(b ** 2 - 4 * a * c)
    return b ** 2 - 4 * a * c


def roots(d, a, b, c):
    if d > 0:
        result = [
            (-b + d ** 0.5) / (2 * a),  # x1
            (-b - d ** 0.5) / (2 * a),  # x2
            ]
    elif d == 0:
        result = [-b / (2 * a)]
    else:
        result = None

    return result


def solv_square(a, b, c):
    return roots(discriminant(a, b, c), a, b, c)


def square_print(a, b, c, roots):
    get_operand = lambda n: "+" if n > 0 else "-"
    get_root = lambda n: int(n) if n.is_integer() else round(n, 4)

    equation = f"{a}x²"

    if b:
        equation += f" {get_operand(b)} {abs(b)}x"

    if c:
        equation += f" {get_operand(c)} {abs(c)}" 

    output = f"Quadratic eqution {equation} "

    if not roots:
        output += "does not have roots."
    elif len(roots) == 2:
        output += f"has these roots: {get_root(roots[0])}, {get_root(roots[1])}."
    elif len(roots) == 1:
        output += f"has this root: {get_root(roots[0])}."

    print(output)


if __name__ == "__main__":
    main()
