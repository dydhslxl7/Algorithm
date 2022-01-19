package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class A_01_19 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] num = new int[9];
        for(int i=0; i<9; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }

        int count = 0;
        int index = 0;
        int max = 0;
        for (int i : num) {
            count++;
            if(i > max) {
                max = i;
                index = count;
            }
        }
        
        bw.write(max+"\n"+index);
        bw.flush();
        bw.close();
        br.close();
    }
}
