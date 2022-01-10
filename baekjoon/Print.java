package baekjoon;

import java.util.Scanner;

/**
 * hello_world
 */
public class Print {

    // 22/01/09
    public static void hello(String[] args) {
        System.out.println("Hello World!");
    }

    // 22/01/10
    public static void print(String[] args) {
        
        int i = 0;
        while(i < 2)
        {
            System.out.println("강한친구 대한육군");
            i++;
        }
    }

    public static void cat(String[] args) {
        System.out.println("\\   /\\");
        System.out.println(" )  ( ')");
        System.out.println("(  /  )");
        System.out.println("\\(__)|");
    }

    public static void plus(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        System.out.println(num1*num2);
    }

    public static void divide(String[] args) {
        Scanner sc = new Scanner(System.in);
        double num1 = sc.nextDouble();
        double num2 = sc.nextDouble();

        System.out.println(num1/num2);
    }

    public static void calc_4(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        System.out.println(num1+num2);
        System.out.println(num1-num2);
        System.out.println(num1*num2);
        System.out.println(num1/num2);
        System.out.println(num1%num2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();

        System.out.println((num1+num2)%num3);
        System.out.println(((num1%num3)+(num2%num3))%num3);
        System.out.println((num1*num2)%num3);
        System.out.println( ((num1%num3)*(num2%num3))%num3 );
    }
}