package baekjoon;

import java.io.*;

public class Q_10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        // 1안
        /* 
        for(char c = 'a'; c<='z'; c++) {
            for(int i=0; i<str.length(); i++) {
                if(str.charAt(i) == c) {
                    System.out.print(i+" ");
                    break;
                }
                else if(i == (str.length()-1)) System.out.print(-1+" ");
            }
        }
        */
        
        // 2안
        StringBuilder sb = new StringBuilder();

        for (char c = 'a'; c <= 'z'; c++) {
            int idx = str.indexOf(c);
            sb.append(idx).append(" ");
        }

        System.out.print(sb);
    }
}