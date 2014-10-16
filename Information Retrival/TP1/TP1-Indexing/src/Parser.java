import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


abstract class Parser {
	String start;
	String FILEPATH;
	RandomAccessFile file;


	public Parser() {
		//		FILEPATH = "D:/Dropbox/M2 DAC/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		//				String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
		try{
			file =new RandomAccessFile(FILEPATH, "r");
			file.seek(0);
		}catch (IOException e) {
			e.printStackTrace();
		}

	}

	abstract Document getDocument(String str);
	//
	//	public byte[] readFromFile(String filePath,int position, int size)
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

		String text;
		int id =0;


		try {

			ArrayList<Integer> I_stack = new ArrayList<Integer>();		
			String line = "";
			while ( (I_stack.size() < 2) ){

				byte b = (byte) file.read();



				if (b == '\n'){ 

					// this is the end of the current line, so prepare to read the next line
					//System.out.println("Read line: " + line);

					if (line.matches(".I [0-9]+")){
		
						String[] splitted = line.split(" ");
						id = Integer.parseInt(splitted[1]);
						I_stack.add((int) file.getFilePointer());
						System.out.println(file.length());
						System.out.println(file.getFilePointer());

					}
					
					
					line = "";
				}
				else {
					line += (char)b;
				}

	
				
				if (file.getFilePointer()==file.length()) {
//					System.out.println("okokok");
					I_stack.add((int) file.getFilePointer());
						
				}

			}

			file.seek(I_stack.get(0));


			int lenght = I_stack.get(1)-I_stack.get(0);
			byte[] bytes = new byte[lenght];

			file.read(bytes);
			text = new String(bytes);
			file.seek(I_stack.get(1)-10);

			doc.text = text;
			doc.from[0]  = I_stack.get(0); //Get the Id of the document
			doc.from[1] = lenght; //get the length of the document

			doc.id = id-1;

		}catch (IOException e) {
			e.printStackTrace();
		}

		return doc;	
	}


}
