import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


abstract class Parser {
	String start;
	String FILEPATH;
	RandomAccessFile file;




	public Parser() {
		//		FILEPATH = "D:/Dropbox/M2 DAC/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
		String FILEPATH ="/home/arda-mint/Documents/M2/Information Retrival/TP1/data/cisi.txt";
		//		String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
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

		ArrayList<Integer> I_from = new ArrayList<Integer>();
		ArrayList<Integer> line_length = new ArrayList<Integer>();
		
//		int[] I_from = new int[2];
//		int[] line_length = new int[2];

		String text;
		int id =0;
//		int[] line_length = new int[2];


		try {


			String line = "";
			int i=0;
			while (i<2 || file.getFilePointer() == file.length() ){

				byte b = (byte) file.read();



				if (b == '\n'){ 

					// this is the end of the current line, so prepare to read the next line
					//System.out.println("Read line: " + line);

					if (line.matches(".I [0-9]+")){
//						System.out.println(line);
					
						line_length.add((int) line.length());
						I_from.add((int) file.getFilePointer());
						

						String[] splitted = line.split(" ");
						id = Integer.parseInt(splitted[1]);
						//						System.out.println(file.length());
						//						System.out.println(file.getFilePointer());
						//						System.out.println(id);
						doc.id=id;
						
						i++;


					}


					line = "";
				}
				else {	line += (char)b;  }


//			

			}
			
//			if (file.getFilePointer()==file.length()) {
//									System.out.println("okokok");
//				I_from.add((int) file.length());
//				line_length.add((int) line.length());
//				//					file.close();
////				System.out.println(line.length());
//
//			}	if (file.getFilePointer()==file.length()) {
//			System.out.println("okokok");
//I_from.add((int) file.length());
//line_length.add((int) line.length());
////					file.close();
////System.out.println(line.length());
//
//}
			
			
			I_from.set(1, I_from.get(1)-line_length.get(1)-1);
//			System.out.println(I_stack.get(1));

//			System.out.println(I_stack.get(1));
			file.seek(I_from.get(0));
			
			


			int lenght = I_from.get(1)-I_from.get(0);
			byte[] bytes = new byte[lenght];

			file.read(bytes);
			text = new String(bytes);
			//			file.seek(I_stack.get(1)-10);

			doc.text = text;

			String lol = Integer.toString(lenght);
			doc.from = I_from.get(0).toString() +":"+ lol ;
//			doc.id = id-1;

			//			doc.id = id-1;
			

		}catch (IOException e) {
			e.printStackTrace();
		}

		return doc;	
	}


}
