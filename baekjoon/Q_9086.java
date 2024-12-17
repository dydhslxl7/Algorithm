package baekjoon;

import java.io.*;

public class Q_9086 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        String st1, st2="";
        for(int i=0; i<n; i++) {
            st1 = br.readLine();
            st2 += st1.charAt(0)+""+st1.charAt(st1.length()-1);
            if(i<n) st2 += "\n";
        }

        System.out.print(st2);
    }
}
