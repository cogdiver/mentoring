import sys

def saludar(name: str) -> str:
    """
    Greets the user by their name.

    This function takes a name as input, prints a greeting message to the console,
    and returns the same greeting as a string.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message that includes the provided name.
    """
    print(f"Hola! {name}")
    return f"Hola! {name}"

# name = "Valentina"
# saludar(name)
# print(sys.argv)
# print(sys.argv[1:])
# print(type(sys.argv))
names = sys.argv[1:]
if not names:
    print("Hola, everyone")

for n in names:
    saludar(n)
