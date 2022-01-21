package baekjoon;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
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
}
