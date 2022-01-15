package baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.IOException;

public class A_01_15 {
    public static void last_for(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n1 = Integer.parseInt(st.nextToken());
        int n2 = Integer.parseInt(st.nextToken());
        
        ArrayList<Integer> al = new ArrayList<Integer>();
        int temp;
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n1; i++) 
        {
            temp = Integer.parseInt(st.nextToken());
            if(temp < n2) {
                al.add(temp);
            }
        }

        for (int i : al) {
            bw.write(i+"\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }

    public static void while1(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayList<Integer> al = new ArrayList<Integer>();
        int i;
        do
        {
            String[] st = br.readLine().split(" ");
            i = Integer.parseInt(st[0])+Integer.parseInt(st[1]);
            if(i != 0) al.add(i);
        } while(i != 0);
        
        for (int j : al) {
            bw.write(j+" ");
        }

        br.close();
        bw.flush();
        bw.close();
    }

}
