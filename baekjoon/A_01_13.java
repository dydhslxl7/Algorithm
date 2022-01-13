package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class A_01_13 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        int num1;
        int num2;
        for(int i=1; i<n+1; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            num1 = Integer.parseInt(st.nextToken());
            num2 = Integer.parseInt(st.nextToken());

            bw.write("Case #"+i+": "+num1+" + "+num2+" = "+(num1+num2)+"\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
