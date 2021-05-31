class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    
    def __init__(self, head):
        self.head = head
 
    def length(self) -> int:
        """ El método que cuenta los elementos de la lista, length(),
            primero comprueba que la lista no esté vacía, y luego recorre
            todos los elementos de la lista incrementando un contador por 
            cada elemento. Al final devuelve el contador:
        """
        current = self.head
        if current is not None:
            count = 1

            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0
    
    def insert(self, data, position):
        """
        El siguiente método, insert(datos, posición), inserta un elemento 
        tras la posición indicada. Si se indica la posición 0, el nuevo 
        elemento pasa a ser la cabecera de la lista. En esta implementación, 
        si la posición que se pasa como argumento excede el tamaño de la lista,
        el elemento se inserta al final:
        """
        new_node = Node(data)

        if position == 0:
            new_node.next = linked_list.head
            linked_list.head = new_node
        else:
            current = linked_list.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node
   
    def delete(self, position):
        """
        El método delete(posición) borra el elemento en la posición pasada como 
        parámetro. Si es el primer elemento la lista de la cabeza pasa a ser el 
        segundo elemento. Si se encuentra el elemento en la lista y se borra devolvemos
        True, en caso contrario devolvemos False:
        """
        if position != 1:
            current = self.head
            k = 1
            while current.next is not None and k < position - 1:
                current = current.next
                k += 1
            if current.next is not None:
                current.next = current.next.next
                return True
            else:
                return False
        else:
            self.head = self.head.next
            return True

    

if __name__ == '__main__':
    #creamos la lista
    linked_list = SinglyLinkedList(Node(1))


    #rellenamos la lista
    for i in range(2,10):
        linked_list.insert(i, i-1)
        

    #insertamos un elemento
    linked_list.insert(999,3)

    
    #eliminamos un elemento
    linked_list.delete(6)

    #mostramos la lista
    current = linked_list.head
    while current is not None:
        print(current.data)
        current = current.next