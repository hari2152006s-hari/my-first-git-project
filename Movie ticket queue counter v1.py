movie_ticket_queue = ["hari", "jonh", "tony"]


def enqueue():
    name = input("Enter the name: ")
    movie_ticket_queue.append(name)
    print(name, "joined the queue.")


def dequeue():
    if len(movie_ticket_queue) == 0:
        print("The queue is empty. No one to serve.")
    else:
        served = movie_ticket_queue.pop(0)
        print(served, "got the ticket.")


def show_queue():
    if len(movie_ticket_queue) == 0:
        print("The queue is empty.")
    else:
        print("Current queue:", movie_ticket_queue)


running = True
while running:
    print("\n1. Add a person")
    print("2. Serve the next person")
    print("3. Show the queue")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        show_queue()
    elif choice == "4":
        running = False
        print("Goodbye!")
    else:
        print("Please enter 1, 2, 3 or 4.")