def draw_square(size):
    for _ in range(size):
        print('* ' * size)

def draw_triangle(size):
    for i in range(1, size + 1):
        print('* ' * i)

def draw_circle(radius):
    for i in range((2 * radius) + 1):
        for j in range((2 * radius) + 1):
            dist = ((i - radius) ** 2 + (j - radius) ** 2) ** 0.5
            if dist < radius:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def main():
    while True:
        print("Choose a shape to draw:")
        print("1. Square")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            size = int(input("Enter the size of the square: "))
            draw_square(size)
        elif choice == '2':
            size = int(input("Enter the size of the triangle: "))
            draw_triangle(size)
        elif choice == '3':
            radius = int(input("Enter the radius of the circle: "))
            draw_circle(radius)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()