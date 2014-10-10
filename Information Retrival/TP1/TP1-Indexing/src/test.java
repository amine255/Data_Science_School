	
//		String FILEPATH = "/home/arda/Documents/Data_Science_School/Information Retrival/TP1/data/cisi.txt";
////		String FILEPATH = "/users/Etu6/3402426/Documents/M2/Information Retrival/TP1/data/cisi.txt";
//		
//			
//		try {
//			
//			RandomAccessFile file = new RandomAccessFile(FILEPATH, "r");
//		
//			long line_id;
//			String line = file.readLine();
//			boolean match_I;
//		
//			ArrayList<Long> I_stack = new ArrayList<Long>();		
//			file.seek(0);
//			
//			
//			while (I_stack.size() != 2) {
//				
//				if (file.readLine().matches(".I [0-9]+")) {
//					
//					line_id = file.getFilePointer();
//
//					I_stack.add(line_id);
//								}
//				
//				file.readLine();
//				
//			}
//			
//			
//			System.out.println(I_stack.size());
//			long diff = I_stack.get(1)-I_stack.get(0);
//			System.out.println(diff);
//			byte[] bytes = new byte[(int) diff];
//			String text_extrait = new String(file.readUTF());	
////			file.seek(I_stack.get(0));
//
//			getDocument();
//			
//			
//		}catch (IOException e) {
//		e.printStackTrace();
//		}
		