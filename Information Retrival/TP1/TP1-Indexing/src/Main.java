import java.util.HashMap;

public class Main {
	
	public static void main(String[] args) {


Parser_cisi arda_parser = new Parser_cisi();


//for (int i=0; i<1;i++){
//	System.out.println("indice i boucle for :" + i);
	Document nextdoc = arda_parser.nextDocument();
//	System.out.println("nextdoc.from"+nextdoc.from);
//	System.out.println("nextdoc.id"+nextdoc.id);
	System.out.println("nextdoc.text "+nextdoc.text);
	System.out.println("=================");
	
//}

//String[] splitted_text = nextdoc.text.split(" ");
//
//
//for (int i=0;i<splitted_text.length;i++){
//	System.out.println(splitted_text[i]);
//	
//	
//}

Stemmer stem = new Stemmer();
HashMap<String,Integer> res = stem.porterStemmerHash(nextdoc.text);

System.out.println(res.values());
//Document getdoc = arda_parser.getDocument(nextdoc.text);

//System.out.println(getdoc.from);
//System.out.println(getdoc.id);
//System.out.println(getdoc.text);

	}

	

	
}