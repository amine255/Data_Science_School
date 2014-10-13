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

String[] splitted_text = nextdoc.text.split(" ");


for (int i=0;i<splitted_text.length;i++){
	System.out.println(splitted_text[i]);
	
	
}

Stemmer stem = new Stemmer();
//String[] arda = "hello bitch i want to be a joke for lol".split(" ");
//String FILEPATH = "D:/Dropbox/M2 DAC/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
//
stem.main(splitted_text);
	
//Document getdoc = arda_parser.getDocument(nextdoc.text);

//System.out.println(getdoc.from);
//System.out.println(getdoc.id);
//System.out.println(getdoc.text);

	}

	

	
}