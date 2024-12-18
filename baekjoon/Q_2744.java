package baekjoon;

import java.io.*;

public class Q_2744 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String str2 = "";
        
        // 1안
        Character c;
        for(int i=0; i<str.length(); i++) {
            c = str.charAt(i);
            if(Character.isUpperCase(c))
                str2 += Character.toString(Character.toLowerCase(c));
            else
                str2 += Character.toString(Character.toUpperCase(c));
        }

        // 2안
        /*
         * Character.toString(str.charAt(i)) -> String로 return
         * .toUpperCase(); -> String클래스의 내장 함수
         */
        for(int i=0; i<str.length(); i++) {
            if(str.charAt(i) >= 'a' && str.charAt(i) <= 'z')
                str2 += Character.toString(str.charAt(i)).toUpperCase();
            else
                str2 += Character.toString(str.charAt(i)).toLowerCase();
        }

        System.out.println(str2);
    }    
}