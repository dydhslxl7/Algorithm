package baekjoon;

import java.io.*;
import java.util.*;

public class Q_2475 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = 0, temp = 0;

        for(int i=0; i<5; i++) {
            temp = Integer.parseInt(st.nextToken());
            n += (temp*temp);
        }

        System.out.print(n%10);
    }
}
