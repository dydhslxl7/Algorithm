package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


// 풀고있음 - error 발생
public class A_01_16 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        String s, str = "";
        while((s = br.readLine()) != null) {

            st = new StringTokenizer(s, " ");
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            
            str += (n1+n2)+"\n";
        }

        System.out.println(str);

        br.close();
    }
}
