package baekjoon;

import java.util.Scanner;

public class A_01_17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int n1, n2, n3, count = 0;
        int result = n;
        
        while(true) {
            
            n1 = result / 10;
            n2 = result % 10;
            n3 = (n1+n2) % 10;
            
            result = n2*10 + n3;
            count++;

            if(result == n) break;
        }
        System.out.println(count);

        sc.close();
    }
}
