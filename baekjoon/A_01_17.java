package baekjoon;

import java.util.Scanner;

public class A_01_17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        StringBuilder sb;
        int n = sc.nextInt();
        int result = 0;
        int n1, n2, n3, count = 0;
        int temp = n;
        
        while(n != result) {
            if(count == 0 && temp < 10) {
                temp *= 2;
            }
            
            n1 = temp / 10;
            n2 = temp % 10;
            n3 = (n1+n2) % 10;
            
            sb = new StringBuilder();
            sb.append(n2);
            sb.append(n3);
            temp = result = Integer.parseInt(sb.toString());

            count++;
        }
        System.out.println(count);
    }
}
