import java.io.*;
import java.util.*;

public class Q_2920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String flag = "";

        // 1안에서 주의
        // countTokens() -> 1 2 3 -> count가 5임. 빈 값도 count에 포함됨.
        int pre = Integer.parseInt(st.nextToken()), pos;
        for(int i=1; i<8; i++) {
            pos = Integer.parseInt(st.nextToken());
            
            if(pre==pos-1) {
                flag = "ascending";
            }
            else if(pre==pos+1) {
                flag = "descending";
            }
            else {
                flag = "mixed"; break;
            }
            
            pre = pos;
        }

        System.out.print(flag);
    }
}