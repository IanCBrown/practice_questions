import java.util.*; 

public class game_of_throws {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 

        int kids = in.nextInt();
        int com = in.nextInt(); 
        in.nextLine(); 
        Stack<Integer> past = new Stack<Integer>(); 
        int curr = 0; 

        for (int i = 0; i < com; i++) {
            String instruction = in.next(); 
            if (instruction.equals("undo")) {
                int num_undos = in.nextInt(); 
                for (int j = 0; j < num_undos; j++) {
                    int last = past.pop() * -1; 
                    curr += last; 
                    while(curr < 0) {
                        curr += kids; 
                    }
                    curr = curr % kids; 
                }
            } else {
                int next = Integer.parseInt(instruction); 
                curr += next; 
                past.push(next);
                while (curr < 0) {
                    curr += kids; 
                }
                curr = curr % kids; 
            }
        }
        System.out.println(curr); 
    }
}