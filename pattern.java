public class pattern{
    public static void main(String[] args) {
        System.out.println("printing pattern in java");
        int n=7;
       
       

        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                boolean condition =   row+col==n;

                if (condition) {
                    System.out.print(" *");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.print(" "); // same as your Python code's end=" "
            System.out.println();  // move to next line
        }
    }
}

    
