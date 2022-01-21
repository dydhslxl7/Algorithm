package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class A_01_21 {
    public static void remainder(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n, n1, n2;
        Integer inte;
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for(int i=0; i<10; i++) {
            n = sc.nextInt();
            n1 = n%42;
            inte = Integer.valueOf(n1);
            
            if( hm.containsKey(inte) ) { // 키 존재
                n2 = hm.get(inte);
                hm.put(n1, n2++);
            } else {
                hm.put(n1, 1);
            }
        }

        System.out.println(hm.size());
        sc.close();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer stz = new StringTokenizer(br.readLine());

        double[] num = new double[n];

        for(int i=0; i<n; i++) {
            num[i] = Double.parseDouble(stz.nextToken());
        }
        
        Arrays.sort(num);

        double total = 0;
        for (double i : num) {
            total += i/num[n-1]*100;
        }

        System.out.println(total/n);
    }
}
