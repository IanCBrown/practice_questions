import java.util.*; 

public class island_hopping {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in); 
        int num_cases = in.nextInt(); 
        for (int q = 0; q < num_cases; q++) {
            // input
            int N = in.nextInt(); 
            Island[] islands = new Island[N]; 

            for (int i = 0; i < N; i++) {
                double x = in.nextDouble(); 
                double y = in.nextDouble(); 
                islands[i] = new Island(x, y); 
            }

            // Do Prim's 
            double[] distances = new double[N];
            for (int i = 0; i < N; i++) {
                distances[i] = Integer.MAX_VALUE; 
            } 
            HashSet<Integer> visited = new HashSet<Integer>(); 
            int current = 0; 
            int count = 1; 
            double total = 0; 
            while (count < N) {
                // visit this island
                visited.add(current); 
                Island currentIsland = islands[current]; 
                // update distances with all the new neighbors 
                for (int i = 0; i < N; i++) {
                    if (i == current) {
                        continue; 
                    }
                    Island otherIsland = islands[i];
                    double newDistance = getDistance(currentIsland, otherIsland); 
                    if (newDistance < distances[i]) {
                        distances[i] = newDistance; 
                    }
                    // distances[i] = Math.min(distances[i], newDistance); 
                }
                // Find the next island 
                int nextIsland = 0; 
                double bestDistance = Integer.MAX_VALUE;
                for (int i = 0; i < N; i++) {
                    if (visited.contains(i)) {
                        continue; 
                    }
                    if (distances[i] < bestDistance) {
                        bestDistance = distances[i]; 
                        nextIsland = i; 
                    }
                    // bestDistance = Math.min(distances[i], bestDistance);                     
                }
                count++; 
                total += Math.sqrt(bestDistance); 
                current = nextIsland; 
            }    
            System.out.println(total); 
        }
    }

    // get distances of two islands 
    static double getDistance(Island a, Island b) {
        double dist = (a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y);
        return dist; 
    }

    public static class Island {
        double x; 
        double y; 
        boolean visited; 

        Island(double a, double b) {
            this.x = a; 
            this.y = b; 
            visited = false;             
        } 
    }



}