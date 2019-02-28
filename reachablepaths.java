import java.util.Scanner;
import java.util.HashSet;

public class reachablepaths {
    
    static int[] graph; 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);  

        int Z = in.nextInt(); 
        // each test case 
        for (int i = 0; i < Z; i++) {
            int cities = in.nextInt(); 
            int roads = in.nextInt(); 

            graph = new int[cities]; 
            for (int j = 0; j < cities; j++) {
                graph[j] = j; 
            }
            // get inputs

            for (int k = 0; k < roads; k++) {
                int a = in.nextInt(); 
                int b = in.nextInt(); 
                union(a,b); 
            }

            // number of disjoint sets - 1 = number of roads needed 
            // number of disjoint sets = number of representative elements 
            HashSet<Integer> uniqueParents = new HashSet<Integer>();
            for (int l = 0; l < cities; l++) {
                uniqueParents.add(find(l)); 
            }
            System.out.println(uniqueParents.size() - 1); 
        }
    }

    static int find(int index) {
        if (graph[index] == index) {
            return index; 
        }
        graph[index] = find(graph[index]); 
        return graph[index]; 
    }

    static void union(int a, int b) {
        int aParent = find(a); 
        int bParent = find(b); 

        if (aParent > bParent) {
            graph[aParent] = bParent; 
        }
        else {
            graph[bParent] = aParent; 
        }
    }

}