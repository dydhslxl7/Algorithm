package baekjoon;

import java.io.*;

public class Q_5597 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] num = new int[31];
        
        for(int i=1; i<29; i++) {
            num[Integer.parseInt(br.readLine())] = 1;
        }

        for(int i=1; i<31; i++) {
            if(num[i] != 1) System.out.println(i);
        }
    }
}