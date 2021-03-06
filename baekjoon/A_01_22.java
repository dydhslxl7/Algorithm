package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A_01_22 {

    public static void OX(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] store = new int[n];
        
        String str;
        for(int i=0; i<n; i++) {
            str = br.readLine();

            int count = 1;
            for(int j=0; j<str.length(); j++) {
                if(str.charAt(j) == 'O') {
                    store[i] += count;
                    count++;
                } else {
                    count = 1;
                }
            }
        }

        for (int i : store) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        double[] persent = new double[n];
        int n2 = 0;
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            n2 = Integer.parseInt(st.nextToken());
            int[] num = new int[n2];

            int score = 0;
            int total = 0;
            for(int j=0; j<n2; j++) {
                score = Integer.parseInt(st.nextToken());
                total += score;
                num[j] = score;
            }

            double averge = total/n2;
            Arrays.sort(num);

            double count = 0;
            for (int j = 0; j < num.length; j++) {
                if(num[j] > averge) {
                    count = n2-j;
                    persent[i] = count/n2*100;
                    break;
                }
            }
        }

        for (double d : persent) {
            System.out.printf("%.3f%%\n", d);
        }
    }
}
