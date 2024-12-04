package baekjoon;

import java.io.*;
import java.util.*;

public class Q_10872 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int A = Integer.parseInt(st.nextToken());
        long B = 1;

        while(A>0)
        {
            B *= A;
            A--;
        }

        System.out.print(B);
    }
}