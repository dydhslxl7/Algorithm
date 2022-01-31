package baekjoon;

import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class A_01_26 {
    //1157
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] num = new int[26];

        String str = in.nextLine().toUpperCase();

        char temp = '?';
        int max = -1;
        for (int i = 0; i < str.length(); i++) {
            num[str.charAt(i)-65]++;

            if(max < num[str.charAt(i)-65]) {
                max = num[str.charAt(i)-65];
                temp = str.charAt(i);
            }
            else if (max == num[str.charAt(i)-65]) {
                temp = '?';
            }
        }

        System.out.println(temp);
        in.close();
    }

    public static void Q_1152(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();

        StringTokenizer st = new StringTokenizer(str);

        System.out.println(st.countTokens());
        
        in.close();
    }

    public static void Q_2908(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        StringTokenizer st = new StringTokenizer(str);
        
        int n2 = st.countTokens();
        int[] num = new int[n2];
        int n = 0;
        for(int i=0; i<n2; i++) {
            n = Integer.parseInt(st.nextToken());
            num[i] += n / 100;
            num[i] += n % 100 / 10 * 10;
            num[i] += n % 10 * 100;
        }
        
        Arrays.sort(num);

        System.out.println(num[n2-1]);

        in.close();
    }
}