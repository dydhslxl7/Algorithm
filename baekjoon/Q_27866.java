package baekjoon;

import java.io.*;

public class Q_27866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine();
        int n = Integer.parseInt(br.readLine());
        System.out.print(st.charAt(n-1));
    }    
}
