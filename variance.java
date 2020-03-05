import java.io.*;
import java.util.*;
// public List extends Collection;
class variance{
    private static List<String[]> readFile(String filename)
{
  List<String []> records = new ArrayList<String []>();
  try
  {
    BufferedReader reader = new BufferedReader(new FileReader(filename));
    String line;
    while ((line = reader.readLine()) != null)
    {
    // List<String> temp = new ArrayList<String>();
     String arr[]=line.split(" ");
    //  System.out.println("arr length"+arr.length);
    records.add(arr);
    }
    reader.close();
    return records;
  }
  catch (Exception e)
  {
    System.err.format("Exception occurred trying to read '%s'.", filename);
    e.printStackTrace();
    return null;
  }
}
public static void main(String args[]){
         List<String []> records = new ArrayList<String[]>();
         records=readFile("C:\\Users\\PRANJUL\\Desktop\\new data\\filtered_data_with_time\\Ftop\\1.txt");
         System.out.println("got data");
        double sumx = 0;
        double sumy = 0;
        double sumz = 0;
        for(int i=0;i<records.size();i++){

            // = new String[5]; 
            String[] myString=records.get(i);
            // System.out.println("printing"+myString.length);
            System.out.println(i+1);
            for(int j=0;j<myString.length;j++){
      System.out.print(myString[j]+" * "); 
   }
   System.out.println();
            sumx += Double.parseDouble(myString[0]); 
            sumy += Double.parseDouble(myString[1]); 
            sumz += Double.parseDouble(myString[2]); 

}
System.out.println("got sum");
System.out.println("sumx "+sumx+"sumy "+sumy+"sumz "+sumz);
            double meanx = (double)sumx /(double)records.size(); 
            double meany = (double)sumy /(double)records.size(); 
            double meanz = (double)sumz /(double)records.size(); 
            System.out.println("got mean");
            double sqDiffx = 0; 
            double sqDiffy = 0;
            double sqDiffz = 0;
        for(int i=0;i<records.size();i++){

            String[] myString= new String[5]; 
            myString=records.get(i);
            sqDiffx += (Double.parseDouble(myString[0]) - meanx) *  (Double.parseDouble(myString[0]) - meanx);

            sqDiffy += (Double.parseDouble(myString[1]) - meany) *  (Double.parseDouble(myString[1]) - meany);

            sqDiffz += (Double.parseDouble(myString[2]) - meanz) *  (Double.parseDouble(myString[2]) - meanz);


}
System.out.println("got var");
double varx=sqDiffx/(double)records.size();
double vary=sqDiffy/(double)records.size();
double varz=sqDiffz/(double)records.size();
System.out.println(varx+" "+vary+" "+varz);
}
}