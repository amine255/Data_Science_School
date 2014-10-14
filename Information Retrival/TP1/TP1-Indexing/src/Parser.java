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
//				String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
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
		
		String text;
		int id =0;
		long from=0;
		

		try {

			ArrayList<Long> I_stack = new ArrayList<Long>();		
			String line = "";

			while (I_stack.size() != 2){
				
				byte b = (byte) file.read();
				if (b == '\n'){ 
					
					// this is the end of the current line, so prepare to read the next line
					//System.out.println("Read line: " + line);
					if (line.matches(".I [0-9]+")){
						String[] splitted = line.split(" ");
						id = Integer.parseInt(splitted[1]);

						I_stack.add(file.getFilePointer());

					}

					line = "";
				}
				else {
					line += (char)b;
				}

			}

			file.seek(I_stack.get(0));
			
			long diff = I_stack.get(1)-I_stack.get(0);
			
			byte[] bytes = new byte[(int) diff-5];

			file.read(bytes);
			text = new String(bytes);
			from = file.getFilePointer();

			
			doc.text = text;
			doc.from  = from;
			doc.id = id-1;

		}catch (IOException e) {
			e.printStackTrace();
		}

		return doc;	
	}


}
