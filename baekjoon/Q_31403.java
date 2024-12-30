package baekjoon;

import java.io.*;

public class Q_31403 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = new String[3];
        
        str[0] = br.readLine();
        str[1] = br.readLine();
        str[2] = br.readLine();

        int ans1, ans2;
        
        ans1 = Integer.parseInt(str[0])+Integer.parseInt(str[1])-Integer.parseInt(str[2]);
        ans2 = Integer.parseInt(str[0]+str[1])-Integer.parseInt(str[2]);

        System.out.println(ans1);
        System.out.println(ans2);
    }
}