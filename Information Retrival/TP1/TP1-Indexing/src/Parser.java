import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


abstract class Parser {
	String start;
	String FILEPATH;
	RandomAccessFile file;




	public Parser() {
		String FILEPATH ="/home/arda-mint/Documents/M2/Information Retrival/TP1/data/cisi.txt";
//				String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
		try{
			file =new RandomAccessFile(FILEPATH, "r");
			file.seek(0);
		}catch (IOException e) {
			e.printStackTrace();
		}

	}
	abstract Document getDocument(String str);

	public Document nextDocument(){	

		Document doc = new Document();

		ArrayList<Integer> I_from = new ArrayList<Integer>();
		ArrayList<Integer> line_length = new ArrayList<Integer>();

		String text;
		int id =0;

		try {

			String line = "";
			int i=0;
			while (i<2 ){

				byte b = (byte) file.read();

				if (b == '\n'){ 

					// this is the end of the current line, so prepare to read the next line
					//System.out.println("Read line: " + line);

					if (line.matches(".I [0-9]+")){

						line_length.add((int) line.length());
						I_from.add((int) file.getFilePointer());


						String[] splitted = line.split(" ");	
						id = Integer.parseInt(splitted[1]);

						doc.id=id;

						i++;

					}

					line = "";
				}
				else {	line += (char)b;  }

				if (file.getFilePointer() == file.length() ){
//					System.out.println("ok================");
//					System.out.println(line.length());
//					System.out.println(file.getFilePointer());
					
					I_from.add((int) file.getFilePointer());
					line_length.add((int) line.length());
					
//					
//					I_from.set(1, I_from.get(1)-line_length.get(1)-1);

					file.seek(I_from.get(0));

					int lenght = I_from.get(1)-I_from.get(0);
					byte[] bytes = new byte[lenght];

					file.read(bytes);
					text = new String(bytes);

					doc.text = text;

					String lol = Integer.toString(lenght);
					doc.from = I_from.get(0).toString() +":"+ lol ;
					
					file.seek(file.length());
					
					return doc;

				}

				//			

			}

			I_from.set(1, I_from.get(1)-line_length.get(1)-1);

			file.seek(I_from.get(0));

			int lenght = I_from.get(1)-I_from.get(0);
			byte[] bytes = new byte[lenght];

			file.read(bytes);
			text = new String(bytes);

			doc.text = text;

			String lol = Integer.toString(lenght);
			doc.from = I_from.get(0).toString() +":"+ lol ;
			doc.id = id-1;


		}catch (IOException e) {
			e.printStackTrace();
		}

		return doc;	
	}


}
