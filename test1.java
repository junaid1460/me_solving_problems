import java.io.*;
import java.util.*;


public class Test {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for(int t_i=0; t_i<T; t_i++)
        {
            String s = br.readLine();

            String out_ = decode(s);
            System.out.println(out_);
         }

         wr.close();
         br.close();
    }

    static String decode(String s){
        int l = s.length();
        char []a = new char[l];
        int left = l /2;
        int right = left + 1;
        boolean even = true;
        
        if(l % 2 == 1){
            a[right - 1] = s.charAt(0);
            right += 1;
        }else{
            a[left - 1] = s.charAt(0);
            left -= 1;
            even = false;
        }
        System.out.println("left:"+left+",right:" + right);
            for(int i =1;i<l;++i){
                System.out.println("left:"+left+",right:" + right);
                if(even){
                    a[left -1] = s.charAt(i);
                    left -= 1;
                }else{
                    a[right  -1] = s.charAt(i);
                    right += 1;
                }
                even = !even;
            }
        

        return new String(a);
        // Write your code here
    
    }
}