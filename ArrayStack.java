public class ArrayStack {
    private int top;
    private int[] arr;

    public ArrayStack(int capacity) {
        this.top = -1;
        this.arr = new int[capacity];
    }

    public void push(int item) {
        if (top + 1 == arr.length) {
            System.out.println("Stack Overflow");
            return;
        }
        top++;
        arr[top] = item;
    }

    public int pop() {
        if (top == -1){
            System.out.println("Stack Underflow");
            return -1;
        }
        int arr1 = arr[top];
        top--;
        return arr1;
    }

    public int peek() {
        if (top == -1){
            return -1;
        }
        return arr[top];
    }

    public void display() {
        if (top==-1){
            System.out.println("Stack is Empty");
            return;
        }
        for(int i=top;i>=0;i--){
            System.out.println(arr[i]);

        }
        
    }

    public static void main(String[] args){
        ArrayStack stack = new ArrayStack(4);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        System.out.println(stack.peek());
        System.out.println();
        stack.push(5);
        System.out.println();
        stack.display();
        stack.pop();
        System.out.println();
        System.out.println(stack.peek());
        System.out.println();
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();


    }
}
