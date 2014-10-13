public class Main {
	
	public static void main(String[] args) {


Parser_cisi arda_parser = new Parser_cisi();


for (int i=0; i<2;i++){
//	System.out.println("indice i boucle for :" + i);
	Document nextdoc = arda_parser.nextDocument();
	System.out.println(nextdoc.from);
	System.out.println(nextdoc.id);
	System.out.println(nextdoc.text);
	
	
}


//Document getdoc = arda_parser.getDocument(nextdoc.text);

//System.out.println(getdoc.from);
//System.out.println(getdoc.id);
//System.out.println(getdoc.text);

	}

	

	
}