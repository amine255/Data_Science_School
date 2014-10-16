import java.io.IOException;
import java.util.HashMap;

public class Main {




	public static void main(String[] args) {


		Parser_cisi arda_parser = new Parser_cisi();
		Stemmer stem = new Stemmer();

		HashMap<Integer,Integer> docs = new HashMap<Integer,Integer>();
		HashMap<String,Integer> stems = new HashMap<String, Integer>();
		HashMap<Integer,String> docFrom = new HashMap<Integer, String>();


//		try {
//			while (arda_parser.file.getFilePointer()!=arda_parser.file.length()) {
								for (int i=0; i<2500;i++){
//					System.out.println("indice i boucle for :" + i);

				Document doc = arda_parser.nextDocument();

					System.out.println("DOC ID :"+doc.id);
					System.out.println("DOC FROM :"+ doc.from);
					System.out.println(doc.text);

//		

				//	System.out.println();
				//	System.out.println(arda_parser.f;
				//	docFrom.put(doc.id,doc.from);
				//	int key =2460;
				////	res.remove(key);
				//	byte[] b = key.getBytes();
				//	
				//	System.out.println(b.hashCode());

			}
//		} 
//		catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}


		//System.out.println(docFrom.containsKey(key));
		//System.out.println(docFrom.entrySet());







	}




}