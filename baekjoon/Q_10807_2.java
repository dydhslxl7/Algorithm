package baekjoon;

import java.io.*;
import java.util.*;

public class Q_10807_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 첫번째 In
        int n = Integer.parseInt(br.readLine());
        
        // 두번째 In
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 세번째 In
        int n2 = Integer.parseInt(br.readLine());
        
        int count = 0;
        for(int i=0; i<n; i++) {
            if(Integer.parseInt(st.nextToken()) == n2) {
                count++;
            }
        }
        
        System.out.print(count);
    }
}