package baekjoon;

import java.util.Scanner;

public class A_02_04 {
    //2750
    public static void sort(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());

        int temp;
        int[] num = new int[n];
        for(int i=0; i<n; i++) {
            num[i] = Integer.parseInt(in.nextLine());

            for(int j=i; j>0; j--) {
                if(num[j] < num[j-1]) {
                    temp = num[j-1];
                    num[j-1] = num[j];
                    num[j] = temp;
                }
            }
        }

        for (int i : num) {
            System.out.println(i);
        }
        in.close();
    }

    //10171
    public static void cat(String[] args) {
        System.out.println("\\    /\\");
		System.out.println(" )  ( ')");
		System.out.println("(  /  )");
		System.out.println(" \\(__)|");  
    }

    //10172
    public static void dog(String[] args) {
        System.out.println("|\\_/|");
		System.out.println("|q p|   /}");
		System.out.println("( 0 )\"\"\"\\");
		System.out.println("|\"^\"`    |");
		System.out.println("||_/=\\\\__|");
    }

}