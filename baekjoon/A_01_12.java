package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/**
 * Main
 */
public class A_01_12 {

    public static void A12_1(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;

        for(int i=0; i<n; i++) {
            
            st = new StringTokenizer(br.readLine(), " ");

            bw.write(Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken()) + "\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int num1;
        int num2;

        try {
            int n = Integer.parseInt(br.readLine());

            for(int i=1; i<=n; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                num1 = Integer.parseInt(st.nextToken());
                num2 = Integer.parseInt(st.nextToken());

                bw.write("Case #"+i+": "+(num1+num2)+"\n");
            }

            br.close();
            bw.flush();
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        } 
    }
}