
abstract class Parser {
	String start;
		
	public Parser(){
		
		
	}
	
	abstract Document getDocument(String str);
	
	
	public Document nextDocument(){
		

		String str = new String("Read till find .I");
		

		Document doc = getDocument(str);
		
		doc.from = 34354;
		doc.id = 3434;
		
		
		return doc;
	}
	
	
	
	

}