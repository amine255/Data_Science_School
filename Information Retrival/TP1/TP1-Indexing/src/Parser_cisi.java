import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.ArrayList;


class Parser_cisi extends Parser{
	

	Parser_cisi() {
		super.start = ".I";
		
		

    }

	
	Document getDocument(String text) {	

		Document  doc = new Document();
		
		doc.text=text;	
		
		
		
		return doc;
	}


	
	
}

