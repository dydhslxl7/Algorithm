package baekjoon;

import java.util.Scanner;
import java.util.Arrays;

public class A_01_18 {
    public static void way1(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] num = new int[n];

        for(int i=0; i<n; i++) {
            num[i] = sc.nextInt();
        }

        sc.close();
        Arrays.sort(num);
        System.out.println(num[0]+" "+num[4]);
    }
}
