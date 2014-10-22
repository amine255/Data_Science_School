import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
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

			HashMap<Integer,Integer> docs = new HashMap<Integer,Integer>();
			HashMap<String,Integer> stems = new HashMap<String, Integer>();
			HashMap<Integer,String> docFrom = new HashMap<Integer, String>();

			int pos = 0;


			String index_index = "/home/arda-mint/Desktop/Link to M2/Information Retrival/TP1/Index/index_index.txt";
			String index_inverted = "/home/arda-mint/Desktop/Link to M2/Information Retrival/TP1/Index/index_inverted.txt";

			RandomAccessFile index= new RandomAccessFile(index_index, "rw");
			RandomAccessFile inverted = new RandomAccessFile(index_inverted, "rw");

			//					while (arda_parser.file.length()!=arda_parser.file.getFilePointer()) {
			for (int i=0; i<2;i++){


				Document doc = arda_parser.nextDocument();

				//						System.out.println("DOC ID :"+doc.id);
				//						System.out.println("DOC FROM :"+ doc.from);
				stems = stem.porterStemmerHash(doc.text);

				remove_star(stems);

				String hash2string = stems.toString();
				byte[] string_byte = hash2string.getBytes("UTF-8");
				System.out.println(string_byte.length);
				int longueur = string_byte.length;

				docs.put(pos,longueur);
				System.out.println(docs.entrySet());

				pos = pos + longueur;
			}//end for



			//					while (arda_parser.file.length()!=arda_parser.file.getFilePointer()) {
			for (int i=0; i<2;i++){


			}//end for

		}//End try





















		catch (IOException e) {e.printStackTrace();}

	}//end public void main
}