import java.util.HashMap;

public class main {
	
	public static void main(String[] args) {


Parser_cisi arda_parser = new Parser_cisi();
Stemmer stem = new Stemmer();

HashMap<Integer,Long> docs = new HashMap<Integer,Long>();
HashMap<String,Integer> stems = new HashMap<String, Integer>();
HashMap<Integer,Integer> docFrom = new HashMap<Integer, Integer>();


//while (true) {
for (int i=0; i<2;i++){
//	System.out.println("indice i boucle for :" + i);
	
	Document doc = arda_parser.nextDocument();
	
//	System.out.println(doc.from);
//	System.out.println(doc.text);
	System.out.println(doc.id);
//	System.out.println(doc.from);
	
//	docs.put(doc.id,doc.from);
//	String key ="DALAN";
////	res.remove(key);
//	byte[] b = key.getBytes();
//	
//	System.out.println(b.hashCode());
	
}

//System.out.println(docs.entrySet());





	}

	

	
}