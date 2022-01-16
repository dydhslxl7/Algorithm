package baekjoon;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s, str="";
        while((s = sc.nextLine()) != "\n") {
            String[] temp = s.split(" ");
System.out.println(temp[0]);
            if(temp != null)
                str += (Integer.parseInt(temp[0])+Integer.parseInt(temp[1]))+"\n";
        }

        System.out.println(str);
    }
}
