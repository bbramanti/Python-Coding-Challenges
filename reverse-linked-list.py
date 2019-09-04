class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next  = None

def reverse(head):
	previous = None
	current = head
	while (current is not None):
		next = current.next
		current.next = previous
		previous = current
		current = next
	return previous

def print_linked_list(head):
	current = head
	while (current is not None):
		print (current.value)
		current = current.next

def main():
	node1 = LinkedListNode(10)
	node2 = LinkedListNode(20)
	node3 = LinkedListNode(30)
	node4 = LinkedListNode(40)
	node1.next = node2
	node2.next = node3
	node3.next = node4
	print_linked_list(node1)
	print ("- - - -")
	print_linked_list(reverse(node1))

  
if __name__== "__main__":
	main()