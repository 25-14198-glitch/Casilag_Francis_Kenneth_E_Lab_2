class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node('Buksan mo by Willie Revillame')
head = node1


def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    if (head == None):
        head == newNode
    else:
        newNode.next = head
        head = newNode


node1 = Node('Buksan mo by Willie Revillame')
head = node1

insertNodeAtTheBeginning('Ale by The Bloomfields')
insertNodeAtTheBeginning('Torpe by Jao')
insertNodeAtTheBeginning('BMW by Because')
insertNodeAtTheBeginning('Fallen by Lola Amour')


def traverseLinkedList():
    current = head
    while (current):
        print(current.data, end=" -> ")
        current = current.next


node1 = Node('Buksan mo by Willie Revillame')
head = node1

insertNodeAtTheBeginning('Ale by The Bloomfields')
insertNodeAtTheBeginning('Torpe by Jao')
insertNodeAtTheBeginning('BMW by Because')
insertNodeAtTheBeginning('Fallen by Lola Amour')
traverseLinkedList()


def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)

    if (head == None):
        head = newNode
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = newNode


def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)

    if (head == None):
        head = newNode
    else:
        current = head.next
        prev = head

        while (prev.data != node):
            prev = current
            current = current.next

            if (current == None):
                print('The node does not exist')
                return

    newNode.next = current
    prev.next = newNode


insertNodeAtTheEnd("See You Again")
insertNodeAtTheEnd("Yellow")

insertNodeAfterGivenNode("Perfect", "See You Again")
traverseLinkedList()