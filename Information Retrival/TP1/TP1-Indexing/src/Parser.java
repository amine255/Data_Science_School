import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


abstract class Parser {
	String start;
		
	public Parser(){
		
		
	}
	
	abstract Document getDocument(String str);
	public byte[] readFromFile(String filePath, int position, int size)
		      throws IOException {

		  RandomAccessFile file = new RandomAccessFile(filePath, "r");
		  file.seek(position);
		  byte[] bytes = new byte[size];
		  file.read(bytes);
		  file.close();
		  
		  
		  return bytes;
		}	
	
	public Document nextDocument(){
		

		
		
//		String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
////	String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
		String FILEPATH = "D:/Dropbox/M2 DAC/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		
	try {
		RandomAccessFile file = new RandomAccessFile(FILEPATH, "r");
	
long line_id;
		String line = file.readLine();
		boolean match_I;
//		byte[] testb = new byte[10];
		ArrayList<Long> I_stack = new ArrayList<Long>();		
		file.seek(0);
	
		while (I_stack.size() != 2) {
			if (file.readLine().matches(".I [0-9]+")) {
//			if (file.readLine().startsWith(".I ")) {
				
				line_id = file.getFilePointer();
//				System.out.println(line_id);
				System.out.println(new String(readFromFile(FILEPATH,(int) line_id-5, 23)));	 

				I_stack.add(line_id);
							}
			
//			System.out.println("ok");
			
		}
		
//		
//System.out.println(I_stack.size());
		
file.seek(I_stack.get(0));
long diff = I_stack.get(1)-I_stack.get(0);
byte[] bytes = new byte[(int) diff-5];

//System.out.println(diff);
file.read(bytes);
String str =new String(bytes);
//System.out.println(str);
		
	}catch (IOException e) {
	e.printStackTrace();
	}

	///////////////////	
	String str1="";
		Document doc = getDocument(str1);
		
		doc.from = 34354;
		doc.id = 3434;
		
		
		return doc;
	}
	
	
	
	

}
