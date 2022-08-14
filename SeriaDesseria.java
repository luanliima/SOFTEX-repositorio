import java.io.*;
 class brinquedo implements Serializable{} //1
class Serializebrinquedo{
     public static void main(String args[]){
   brinquedo c = new brinquedo(); 

  try{
FileOutputStream fo = new FileOutputStream("test.ser");
ObjectOutputStream oo = new ObjectOutputStream(fo);
   oo.writeObject(c); 
    oo.close();
System.out.println("Class brinquedo - object serializado com sucesso");  }
  catch(Exception e){e.printStackTrace();}         

 try{
    FileInputStream fi = new FileInputStream("test.ser");
    ObjectInputStream oi = new ObjectInputStream(fi);
    c =(brinquedo) oi.readObject();
    oi.close();
System.out.println("agora ele foi des-serializado com sucesso");
 }catch(Exception e){e.printStackTrace();}          }}
