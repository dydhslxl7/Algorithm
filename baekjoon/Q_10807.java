package baekjoon;

import java.io.*;
import java.util.*;

public class Q_10807 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int[] num = new int[n];
        
        StringTokenizer st2 = new StringTokenizer(br.readLine());

        StringTokenizer st3 = new StringTokenizer(br.readLine());
        int n2 = Integer.parseInt(st3.nextToken());
        int count = 0;
        for(int i=0; i<n; i++) {
            num[i] = Integer.parseInt(st2.nextToken());
            if(num[i] == n2) {
                count++;
            }
        }
        System.out.print(count);
    }
}