import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Set;

public class Main {


	static RandomAccessFile index;
	static RandomAccessFile inverted;

	public Main(){


	}

	public static void remove_star(HashMap stems){

		String key =" * ";
		stems.remove(key);


	}

	public void indexation(){
		try {

			Parser_cisi arda_parser = new Parser_cisi();
			Stemmer stem = new Stemmer();

			HashMap<Integer,String> docs = new HashMap<Integer,String>();
			HashMap<String,Integer> stems = new HashMap<String, Integer>();
			HashMap<String,String> test = new HashMap<String, String>();
			HashMap<Integer,String> docFrom = new HashMap<Integer, String>();

			int pos = 0;


			String index_filepath = "/home/arda-mint/Desktop/Link to M2/Information Retrival/TP1/Index/index_index.txt";
			String inverted_filepath = "/home/arda-mint/Desktop/Link to M2/Information Retrival/TP1/Index/index_inverted.txt";

			//			String index_index = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/Index/index_index.txt";
			//			String index_inverted = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/Index/index_inverted.txt";

			index= new RandomAccessFile(index_filepath, "rw");
			inverted = new RandomAccessFile(inverted_filepath, "rw");

			while (arda_parser.file.length()!=arda_parser.file.getFilePointer()) {
				//			for (int i=0; i<2;i++){

				Document doc = arda_parser.nextDocument();

				stems = stem.porterStemmerHash(doc.text);
				remove_star(stems);

				String stems_string = stems.toString().substring(1, stems.toString().length()-1);
				String regex = "(,\\s)"; 
				String[] splitted = stems_string.split(regex);//getting : "word=doc_freq"

				for (int j=0;j<splitted.length;j++){

					String word = splitted[j].split("=")[0]; //getting : "word"
					String doc_freq = splitted[j].split("=")[1]; // getting : "doc_freq"
					String values =  doc.id + ":" + doc_freq + ";"; // getting : "doc_id:freq;"

					//					System.out.println(one_line);
					//					System.out.println(splitted[j]);
					//					System.out.println(test.get(word));

					if ( test.get(word) == null  ){
						test.put(word, values);
					}
					else {
						//						System.out.println(word);
						//						System.out.println(test.get(word));
						test.put(word, test.get(word) + values);
					}

				}// end for



				//				Filling docFrom || Key = doc.id || Value = "Position:Length" ||
				docFrom.put(doc.id, doc.from);


				// Filling docs || Key = doc.id || Value = "Position:Length" || in the index file
				String hash2string = doc.id+":"+stems.toString()+"\n";

				byte[] string_byte = hash2string.getBytes("UTF-8");

				int longueur = string_byte.length;

				docs.put(doc.id,pos+":"+longueur);

				index.seek(pos);
				index.write(string_byte);

				pos = pos + longueur;




				System.out.println(arda_parser.file.length() + "/" + arda_parser.file.getFilePointer());

			}//end for

			String full_string = test.toString().substring(1, test.toString().length()-1);
			String final_string_splitted = full_string.replaceAll(";, ","\n");

			byte[] string_byte = final_string_splitted.getBytes("UTF-8");

			inverted.seek(0);
			inverted.write(string_byte);


			index.close();
			inverted.close();

		}//End try



		catch (IOException e) {e.printStackTrace();}



	}//END indexation


	public static void main(String[] args) {

		try {


			//			SECOND PASS THROUGH INVERTED INDEX
			String line = "";
			int i=0;


			byte b;

			b = (byte) inverted.read();


			if (b == '\n'){ 

				// this is the end of the current line, so prepare to read the next line
				System.out.println("Read line: " + line);

				if (line.matches(".I [0-9]+")){


				}

				line = "";
			}
			else {	line += (char)b;  }


			//			S
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}//end public void main
}