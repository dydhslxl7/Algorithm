package baekjoon;

import java.io.*;
import java.util.*;

public class Q_10250_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int num = Integer.parseInt(br.readLine());

        for(int i=0; i<num; i++) {
            st = new StringTokenizer(br.readLine());
            
            int h = Integer.parseInt(st.nextToken());
            st.nextToken();
            int n = Integer.parseInt(st.nextToken());
            
            if(n % h == 0) {
                sb.append((h * 100)+(n / h)).append("\n");
            }
            else {
                sb.append((n % h * 100)+(n / h + 1)).append("\n");
            }
        }

        System.out.print(sb);
    }    
}