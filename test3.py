import java.util.EmptyStackException;

class QueueUsingStacks {
    private Stack stack1; // for enqueue operation
    private Stack stack2; // for dequeue operation

    public QueueUsingStacks() {
        stack1 = new Stack();
        stack2 = new Stack();
    }

    public void enqueue(int item) {
        stack1.push(item);
    }

    public int dequeue() {
        if (stack1.isEmpty() && stack2.isEmpty()) {
            throw new EmptyStackException();
        }

        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.pop();
    }

    public int peek() {
        if (stack1.isEmpty() && stack2.isEmpty()) {
            throw new EmptyStackException();
        }

        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.peek();
    }

    public boolean isEmpty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }

    public int size() {
        return stack1.size() + stack2.size();
    }

    private class Stack {
        private int[] array;
        private int top;
    
        public Stack() {
            array = new int[100]; // or any other initial capacity
            top = -1;
        }
    
        public void push(int item) {
            if (top == array.length - 1) {
                int[] newArray = new int[array.length * 2];
                System.arraycopy(array, 0, newArray, 0, array.length);
                array = newArray;
            }
    
            array[++top] = item;
        }
    
        public int pop() {
            if (isEmpty()) {
                throw new EmptyStackException();
            }
    
            return array[top--];
        }
    
        public int peek() {
            if (isEmpty()) {
                throw new EmptyStackException();
            }
    
            return array[top];
        }
    
        public boolean isEmpty() {
            return top == -1;
        }
    
        public int size() {
            return top + 1;
        }
    }
}
