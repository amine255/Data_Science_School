import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


abstract class Parser {
	String start;
	String FILEPATH;
	RandomAccessFile file;
	long pos;


	public Parser() {
//		FILEPATH = "D:/Dropbox/M2 DAC/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
//		String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";

		try{
			file =new RandomAccessFile(FILEPATH, "r");
			file.seek(0);
			pos = file.getFilePointer();
		}catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	abstract Document getDocument(String str);

		public byte[] readFromFile(String filePath,int position, int size)
				throws IOException {
			RandomAccessFile file = new RandomAccessFile(filePath, "r");
			file.seek(position);
			byte[] bytes = new byte[size];
			file.read(bytes);
			file.close();
	
	
			return bytes;
		}	

	public Document nextDocument(){	
		
		Document doc = new Document();
		String str;
		int id = 0;
		long from = 0;
		byte[] b = new byte[5];
		
		try {


			long line_id;
		
			ArrayList<Long> I_stack = new ArrayList<Long>();		
			
			
			while (I_stack.size() != 2) {
				file.read(b);
				String phrase = new String(b);
//				System.out.println(phrase);
				if (phrase.matches(".I")) {
					System.out.println("ok");
					String[] splitted = phrase.split(".I d");
					
//					System.out.println(splitted[1]);
//					String[] splitted = file.readLine().split(".I ");

//					int foo = Integer.parseInt(splitted[1]);
					
					
					line_id = file.getFilePointer();

						 

					I_stack.add(line_id);
				}

				//			System.out.println("ok");
				file.readLine();
//				System.out.println("ok");
			}
			
			file.seek(I_stack.get(0));
			long diff = I_stack.get(1)-I_stack.get(0);
			byte[] bytes = new byte[(int) diff-5];

			//			System.out.println(diff);
			file.read(bytes);
			str = new String(bytes);

			doc.text = str;
			doc.from  = file.getFilePointer();			
		
		}catch (IOException e) {
			e.printStackTrace();
		}

		return doc;	
	}


}
