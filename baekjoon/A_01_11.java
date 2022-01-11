package baekjoon;

import java.util.Scanner;

public class A_01_11 {

    public static void multi(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n1 = sc.nextInt();
        int n2 = sc.nextInt();

        int[] key = new int[3];
        key[0] = n2%10;
        key[1] = n2%100/10;
        key[2] = n2/100;

        int num1 = n1*key[0];
        int num2 = n1*key[1]*10;
        int num3 = n1*key[2]*100;

        int result = num1+num2+num3;

        System.out.println(n1*key[0]);
        System.out.println(n1*key[1]);
        System.out.println(n1*key[2]);
        System.out.println(result);

        sc.close();
    }

    public static void grade(String[] args) {
        Scanner sc = new Scanner(System.in);

        String grade;
        int score = sc.nextInt();

        if(score >= 90 && score <= 100) {
            grade = "A";
        } else if(score >= 80 && score <= 89) {
            grade = "B";
        } else if(score >= 70 && score <= 79) {
            grade = "C";
        } else if(score >= 60 && score <= 69) {
            grade = "D";
        } else {
            grade = "F";
        }

        System.out.println(grade);

        sc.close();
    }

    public static void quarter(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        int q;
        if(a > 0 && b > 0) {
            q = 1;
        } else if(a < 0 && b > 0) {
            q = 2;
        } else if(a < 0 && b < 0) {
            q = 3;
        } else {
            q = 4;
        }

        System.out.println(q);

        sc.close();
    }

    public static void clock(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();

        if(m-45 < 0) {
            --h;
            if(h < 0) {
                h = 24 + h;
            }
            m = 60 - (45-m);
        } else {
            m = m - 45;
        }

        System.out.println(h+" "+m);

        sc.close();
    }

    public static void multi_table(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i=1; i<10; i++) {
            System.out.println(n+" * "+i+" = "+(n*i));
        }

        sc.close();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int r_num = sc.nextInt();
        
        int[] num = new int[r_num];
        int num1;
        int num2;

        for(int i=0; i<r_num; i++) {
            num1 = sc.nextInt();
            num2 = sc.nextInt();
            
            num[i] = num1 + num2;
        }
        
        for(int i=0; i<r_num; i++) {
            System.out.println(num[i]);
        }

        sc.close();
    }
}