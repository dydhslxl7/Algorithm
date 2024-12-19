package baekjoon;

import java.io.*;
// import java.util.*;

public class Q_2754 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        Double score = 0.0;

        // 1안
        /*  
        switch(str.charAt(0)) {
            case ('A'): break;
        }
        */

        // 2안
        if(str.charAt(0) == 'A') {
            if(str.charAt(1) == '+') score = 4.3;
            else if(str.charAt(1) == '0') score = 4.0;
            else score = 3.7;
        }
        else if(str.charAt(0) == 'B') {
            if(str.charAt(1) == '+') score = 3.3;
            else if(str.charAt(1) == '0') score = 3.0;
            else score = 2.7;
        }
        else if(str.charAt(0) == 'C') {
            if(str.charAt(1) == '+') score = 2.3;
            else if(str.charAt(1) == '0') score = 2.0;
            else score = 1.7;
        }
        else if(str.charAt(0) == 'D') {
            if(str.charAt(1) == '+') score = 1.3;
            else if(str.charAt(1) == '0') score = 1.0;
            else score = 0.7;
        }
        else if(str.charAt(0) == 'F') {
            score = 0.0;
        }
        
        System.out.print(score);
        
        
        // HashMap으로는 오답처리.
        /*
         * 1. Map은 인터페이스이기 때문에 생성이 불가능함.
         * 2. 그럼에도 Map으로 선언하는 이유는 유연성을 위해서임.
         *    -> 추후 TreeMap 등으로 변경 가능.
         */
        /*
        Map<String, Double> grade = new HashMap<>();
        
        grade.put("A.+", 4.3);
        grade.put("A0", 4.0);
        grade.put("A-", 3.7);
        grade.put("B.+", 3.3);
        grade.put("B0", 3.0);
        grade.put("B-", 2.7);
        grade.put("C.+", 2.3);
        grade.put("C0", 2.0);
        grade.put("C-", 1.7);
        grade.put("D.+", 1.3);
        grade.put("D0", 1.0);
        grade.put("D-", 0.7);
        grade.put("F", 0.0);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print(grade.get(br.readLine()));
        */
    }   
}
