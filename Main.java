import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void star(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for(int i=0; i<n; i++) {
            String st = "";
            for(int j=0; j<=i; j++) {
                st += "*";
            }
            bw.write(st+"\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for(int i=1; i<=n; i++) {
            String st = "";
            
            for(int j=n; j>=1; j--) {
                if(j>i) {
                    st += " ";
                } else {
                    st += "*";
                }
            }

            bw.write(st+"\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
