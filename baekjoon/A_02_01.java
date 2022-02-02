package baekjoon;

import java.util.Scanner;

public class A_02_01 {
    //10926
    public static void question(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println(in.nextLine()+"??!");

        in.close();
    }

    //18108
    public static void year_change(String[] args) {
        Scanner in = new Scanner(System.in);

        int year = Integer.parseInt(in.nextLine())-543;
        System.out.println(year);

        in.close();
    }
}
