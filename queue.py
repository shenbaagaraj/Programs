queue = []
def enqueue():
    element = input("Enter the number : ")
    queue.append(element)
    print(element,"is added to queue","the list values are",queue)
    
        
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        el = queue.pop(0)
        print("removed element :",el)

def shown_answer():
    print(queue)

while True:
    print("Choice 1 = enqueue, choice 2 = dequeue, choice 3 = shown_answer")
    choice = int(input("Enter the choice : "))
    if choice ==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        shown_answer()

    else:
        print("Enter the correct operation number!")
        break
