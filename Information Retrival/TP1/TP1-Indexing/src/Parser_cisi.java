import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


public class Parser_cisi {
	String phrase;
	
	
	public Parser_cisi(){
	
		String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
//		String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
			
		try {
			RandomAccessFile file = new RandomAccessFile(FILEPATH, "r");

			long line_id;
			String line = null;
			boolean match_I;

			ArrayList<Long> I_stack = new ArrayList<Long>();		
			file.seek(0);
			
			while ( (line = file.readLine()) != null) {
//				System.out.println(line + line.length());
				match_I = line.matches(".I [0-9]+");

				if (match_I){
					line_id = file.getFilePointer();
					I_stack.add(line_id);
					
					
				}
			}
			
			System.out.println(I_stack.size());
			System.out.println("finish");
			long diff = I_stack.get(5)-I_stack.get(0);
			
			byte[] bytes = new byte[50];
//			System.out.println(bytes);
			file.seek(I_stack.get(0));
			System.out.println(I_stack.get(0));
			System.out.println(new String(bytes));
//			this.phrase = new String(bytes);
			
			
			
		}catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

//	
//	public void Document(){
//		
//		
//
////		
//}
	
}


