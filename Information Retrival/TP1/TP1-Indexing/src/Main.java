import java.io.IOException;
import java.util.HashMap;

public class Main {




	public static void main(String[] args) {


		Parser_cisi arda_parser = new Parser_cisi();
		Stemmer stem = new Stemmer();

		HashMap<Integer,Integer> docs = new HashMap<Integer,Integer>();
		HashMap<String,Integer> stems = new HashMap<String, Integer>();
		HashMap<Integer,String> docFrom = new HashMap<Integer, String>();


		try {
			while (arda_parser.file.length()!=arda_parser.file.getFilePointer()) {
//												for (int i=0; i<2600;i++){
													

				Document doc = arda_parser.nextDocument();

				System.out.println("DOC ID :"+doc.id);
//				System.out.println("DOC FROM :"+ doc.from);
				//					System.out.println(arda_parser.file.length());
//				System.out.println(doc.text);

				if (doc.id == 2460) {
					System.out.println(doc.text);
					
				}
			}
		} 
		catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}




}