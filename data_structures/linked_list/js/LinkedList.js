class LinkedListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  prepend(value) {
    // create new Node
    const newNode = new LinkedListNode(value);

    // if no head exists, make this the head
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return this
    }

    newNode.next = this.head
    this.head = newNode;

    return this;
  }

  append(value) {
    const newNode = new LinkedListNode(value);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return this;
    }

    this.tail.next = newNode;
    this.tail = newNode;

    return this;
  }

  delete(value) {
    if (!this.head) return null;

    let deletedNode = null;
    let currentNode = this.head;

    while (currentNode) {
      if (currentNode.value === value) {
        deletedNode = currentNode;

        if (deletedNode === this.head) {
          this.head = deletedNode.next;
          if (this.head) this.head.prev = null;
        }
        if (deletedNode === this.tail) this.tail = null;
      } else if (deletedNode === this.tail) {
        this.tail = deletedNode.prev;
        this.tail.next = null;
      } else {
        const prevNode = deletedNode.prev;
        const nextNode = deletedNode.next;

        prevNode.next = nextNode;
        nextNode.prev = prevNode;
      }
    }

    return deletedNode;
  }

  find(value) {
    if (!this.head || !value) return null;

    let currentNode = this.head;

    while (currentNode) {
      if (currentNode.value === value) return currentNode;
    }

    return null;
  }

  deleteTail() {
    if (!this.tail) return null;

    if (this.head === this.tail) {
      const deletedTail = this.tail;
      this.head = null;
      this.tail = null;
      return deletedTail;
    }

    const deletedTail = this.tail;
    this.tail = this.tail.prev;
    this.tail.next = null;
    return deletedTail;
  }

  deleteHead() {
    if (!this.head) return null;

    const deletedHead = this.head;

    if (this.head.next) {
      this.head = this.head.next;
      this.head.prev = null;
    } else {
      this.head = null;
      this.tail = null;
    }

    return deletedHead;
  }
}

let my_list = new DoublyLinkedList();

my_list.append(2);
my_list.prepend(1);
console.log(my_list.head);
