import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Set;

public class Main {

	public static void remove_star(HashMap stems){

		String key =" * ";
		stems.remove(key);


	}




	public static void main(String[] args) {
		try {

			Parser_cisi arda_parser = new Parser_cisi();
			Stemmer stem = new Stemmer();

			HashMap<Integer,String> docs = new HashMap<Integer,String>();
			HashMap<String,Integer> stems = new HashMap<String, Integer>();
			HashMap<Integer,String> docFrom = new HashMap<Integer, String>();

			int pos = 0;


			//			String index_index = "/home/arda-mint/Desktop/Link to M2/Information Retrival/TP1/Index/index_index.txt";
			//			String index_inverted = "/home/arda-mint/Desktop/Link to M2/Information Retrival/TP1/Index/index_inverted.txt";

			String index_index = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/Index/index_index.txt";
			String index_inverted = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/Index/index_inverted.txt";




			RandomAccessFile index= new RandomAccessFile(index_index, "rw");
			RandomAccessFile inverted = new RandomAccessFile(index_inverted, "rw");

			//					while (arda_parser.file.length()!=arda_parser.file.getFilePointer()) {
			for (int i=0; i<2;i++){


				Document doc = arda_parser.nextDocument();


				stems = stem.porterStemmerHash(doc.text);
				remove_star(stems);
				
				System.out.println(stems.toString());

				String stems_string = stems.toString().replaceAll("{", "");

				String regex = ",\\s"; 
				String[] splitted = stems_string.split(regex);//getting : "word=doc_freq"
				System.out.println(splitted.length);


				for (int j=0;j<splitted.length;j++){

					String word = splitted[j].split("=")[0]; //getting : "word"
					String doc_freq = splitted[j].split("=")[1]; // getting : "doc_freq"


					String one_line = word+":"+doc.id+"="+doc_freq+";";
					System.out.println(one_line);



				}









				//Filling docFrom : Key = doc.id, Value = "Position:Length"
				docFrom.put(doc.id, doc.from);





				// Filling docs : Key = doc.id, Value = "Position:Length" // in the index file
				String hash2string = doc.id+":"+stems.toString()+"\n";

				//				System.out.println(hash2string);
				byte[] string_byte = hash2string.getBytes("UTF-8");
				//				System.out.println(string_byte.length);
				int longueur = string_byte.length;

				docs.put(doc.id,pos+":"+longueur);
				//				System.out.println(docs.entrySet());

				index.seek(pos);
				index.write(string_byte);

				pos = pos + longueur;






			}//end for
			//
			//System.out.println(docs.entrySet());
			//System.out.println(docFrom.entrySet());



			//					while (arda_parser.file.length()!=arda_parser.file.getFilePointer()) {
			//			for (int i=0; i<1;i++){
			//				
			//				index.seek(0);
			//				byte[] b = 
			////					index.write(b);
			//				
			//				
			//			}//end for

		}//End try





















		catch (IOException e) {e.printStackTrace();}

	}//end public void main
}