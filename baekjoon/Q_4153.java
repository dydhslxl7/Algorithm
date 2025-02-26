package baekjoon;

import java.io.*;
import java.util.*;

public class Q_4153 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String s; 
        StringBuilder sb = new StringBuilder();

        while(!(s=br.readLine()).equals("0 0 0")) {
            st = new StringTokenizer(s);
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int n3 = Integer.parseInt(st.nextToken());

            int max = 0;
            if(Math.max(n1, n2) == n1) {
                if(Math.max(n1, n3) == n1) max = n1;
                else max = n3;
            }
            else {
                if(Math.max(n2, n3) == n2) max = n2;
                else max = n3;
            }
            
            if(((n1*n1)+(n2*n2)+(n3*n3)-(max*max))==(max*max))
                sb.append("right\n");
            else
                sb.append("wrong\n");
        }

        System.out.print(sb);
    }
}