package baekjoon;

import java.io.*;
import java.util.*;

public class Q_15964 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // int로 선언해도 30점 나옴.
        Long x = Long.parseLong(st.nextToken());
        Long y = Long.parseLong(st.nextToken());
        System.out.print((x+y)*(x-y));
    }
    
    // 결과 30점 나옴.
    /*
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = temp(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        System.out.print(n);
    }

    public static int temp(int x, int y) {
        return (x+y)*(x-y);
    }
    */
}
