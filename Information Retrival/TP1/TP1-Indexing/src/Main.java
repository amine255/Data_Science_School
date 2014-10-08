import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

	
	private static byte[] readFromFile(String filename, long position, int size)
			throws IOException {
		
		RandomAccessFile file = new RandomAccessFile(filename, "r");
		file.seek(position);
		byte[] bytes = new byte[size];
		file.read(bytes);
		file.close();
		
		return bytes;
		

	}
	
//	private static void writeToFile(String filePath, String data, int position)
//			throws IOException {
//
//		RandomAccessFile file = new RandomAccessFile(filePath, "rw");
//		file.seek(position);
//		file.write(data.getBytes());
//		file.close();
//
//	}
	
	
	public static void main(String[] args) {

	String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
//	String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
		
		try {

//			
//			System.out.println(Phrase);
			
			RandomAccessFile file = new RandomAccessFile(FILEPATH, "r");

			long line_id;
			boolean match_I;
			String line = new String(file.readLine());
			
			ArrayList<Long> I_stack = new ArrayList<Long>();		
			file.seek(0);
			
			for (int i=0; i < 3 ;i++)   {
				while (line != null) {
					
					match_I= line.matches(".I [0-9]+");
				 
					if (match_I)  {
						line_id = file.getFilePointer();
						I_stack.add(line_id);

										
					}
					
					}
				
			}
		
			
//			System.out.println(I_stack.size());
//			System.out.println("finish");
//			long diff = I_stack.get(1)-I_stack.get(0);
//			
//			byte[] bytes = new byte[(int) diff];
//			
//			file.seek(I_stack.get(0));
//			
////			String text = new String(file.read(bytes));
//			file.read(bytes);
//			System.out.println( new String(bytes));

			
			
				
			
			//writeToFile(FILEPATH, "hello bros", 22);
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	

	
}