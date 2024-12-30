package baekjoon;

import java.io.*;
import java.util.*;

public class Q_10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int num = Integer.parseInt(br.readLine());

        int[] temp = new int[3];
        String[] ans = new String[num];

        for(int i=0; i<num; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j=0; j<3; j++) {
                temp[j] = Integer.parseInt(st.nextToken());
            }
            
            String x = String.format("%2s", Integer.toString((temp[2] / temp[0])+1)).replace(" ", "0");
            String y = Integer.toString(temp[2] % temp[0]);

            ans[i] = y.concat(x);
        }

        for(String tmp : ans) {
            System.out.println(tmp);
        }
    }    
}