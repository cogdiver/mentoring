import argparse

def main():
    # Crear el parser
    parser = argparse.ArgumentParser(description="Este programa saluda al usuario.")

    # Agregar argumentos
    parser.add_argument('--name', type=str, help='El nombre del usuario', required=True)
    parser.add_argument('--age', type=int, help='La edad del usuario', required=False, default=18)

    # Parsear los argumentos
    args = parser.parse_args()

    # Usar los argumentos
    print(f"Hola, {args.name}!")
    if args.age:
        print(f"Tienes {args.age} años.")

if __name__ == "__main__":
    main()
