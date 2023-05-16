import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String args[]) throws IOException
    {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] weight_answer = new int[N];
        int[] arrOfWeight = new int[N];
        int result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i <= N-1; i++) {
            arrOfWeight[i] = Integer.parseInt(st.nextToken());
        }
        
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(arrOfWeight[a-1] > arrOfWeight[b-1]) {
                weight_answer[b-1] = 1;
            }else if (arrOfWeight[a-1] < arrOfWeight[b-1]){
                weight_answer[a-1] = 1;
            }else {
                weight_answer[a-1] = 1;
                weight_answer[b-1] = 1;
            }
        } 
        for (int answer : weight_answer) {
            if(answer == 0) {
                result += 1;
            }
        }
        System.out.print(result);
    }
}
