import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


abstract class Parser {
	String start;
	String FILEPATH;
	RandomAccessFile file;
	long pos;


	public Parser() {
		FILEPATH = "D:/Dropbox/M2 DAC/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		try{
			file =new RandomAccessFile(FILEPATH, "r");
			file.seek(0);
			pos = file.getFilePointer();
		}catch (IOException e) {
			e.printStackTrace();
		}
		//String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		//String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";

	}

	abstract Document getDocument(String str);

	//	public byte[] readFromFile(String filePath, int position, int size)
	//			throws IOException {
	//		RandomAccessFile file = new RandomAccessFile(filePath, "r");
	//		file.seek(position);
	//		byte[] bytes = new byte[size];
	//		file.read(bytes);
	//		file.close();
	//
	//
	//		return bytes;
	//	}	

	public Document nextDocument(){	
		Document doc = new Document();
		String str;
		int id = 0;
		long from = 0;
		
		try {

			//			this.FILEPATH
			//			RandomAccessFile file = new RandomAccessFile(FILEPATH, "r");

			long line_id;
			//			System.out.println(file.getFilePointer());
			//			System.out.println(file.getFilePointer());

			//			file.seek(line_id);
			//			file.seek(0);
			boolean match_I;

			ArrayList<Long> I_stack = new ArrayList<Long>();		

			while (I_stack.size() != 2) {
				if (file.readLine().matches(".I [0-9]+")) {
					//				if (file.readLine().startsWith(".I ")) {

					line_id = file.getFilePointer();
					//System.out.println(line_id);
					//System.out.println(new String(readFromFile(FILEPATH,(int) line_id-5, 23)));	 

					I_stack.add(line_id);
				}

				//			System.out.println("ok");

			}
			
			file.seek(I_stack.get(0));
			long diff = I_stack.get(1)-I_stack.get(0);
			byte[] bytes = new byte[(int) diff-5];

			//			System.out.println(diff);
			file.read(bytes);
			str = new String(bytes);
//			System.out.println(str);
			//			file.seek(I_stack.get(1));

//			String str1="";
			doc.text = str;
			doc.from = 34354;
			doc.id = 3434;
			
		}catch (IOException e) {
			e.printStackTrace();
		}

		
		
		return doc;


		
	}





}
