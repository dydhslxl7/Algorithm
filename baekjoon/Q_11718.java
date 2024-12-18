package baekjoon;

import java.io.*;

public class Q_11718 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        while((str=br.readLine()) != null) {
            System.out.println(str);
        }
    }
}

/*
 * 1. 배열을 이용해서 해결했을 때 런타임 에러 발생.
 * 2. br.readLine != "" 출력 초과 에러 발생.
 */