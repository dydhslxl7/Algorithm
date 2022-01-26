package baekjoon;

import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    //1157
    // public static void main(String[] args) {
    //     Scanner in = new Scanner(System.in);

    //     String str = in.nextLine().toLowerCase();

    //     char temp;
    //     int n;
    //     HashMap<Character, Integer> hm = new HashMap<>();
    //     for (int i = 0; i < str.length(); i++) {
    //         temp = str.charAt(i);
    //         if(hm.containsKey(temp)) {
    //             n = hm.get(temp);
    //             hm.put(temp, n);
    //         } else {
    //             hm.put(temp, 1);
    //         }
    //     }
        
    //     for(int i=0; i<hm.size(); i++) {

    //     }
    // }

    public static void Q_1152(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();

        StringTokenizer st = new StringTokenizer(str);
        
        int count = 0;

        System.out.println(st.countTokens());
        
        in.close();
    }
}