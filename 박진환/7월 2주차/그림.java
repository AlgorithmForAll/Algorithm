package test_java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 그림 {
	
	   static int n, m;
	   static int[][] arr;

/*		6 5
	    1 1 0 1 1
	    0 1 1 0 0
	    0 0 0 0 0
	    1 0 1 1 1
	    0 0 1 1 1	
	    0 0 1 1 1   */
	   
/*		2 2
	    0 0
	    1 0
	       */	   
	public static void main(String[] args) throws IOException {
		
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
     StringTokenizer st = new StringTokenizer(bf.readLine());
     n = Integer.parseInt(st.nextToken());
     m = Integer.parseInt(st.nextToken());
     int x=0;
		int y=0;
		
     arr = new int[n][m];
  
     
     for(int i=0; i<n; i++){
         st = new StringTokenizer(bf.readLine());
         for(int j=0; j<m; j++){
             arr[i][j] = Integer.parseInt(st.nextToken());
         }
     }
   
     int paintCount=0;
     int paintArea=0;
     
     for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				 List<int[]> list = new ArrayList<>();
				if(arr[i][j]==1){
					paintCount++;
					int[] indexArray = {i,j}; 
					
					arr[i][j]= -1;
					list.add(indexArray);
				
					for (int k = 0; k < list.size(); k++) {
						x=list.get(k)[0];
						y=list.get(k)[1];
						
						
						
						if(x-1>-1){	
							if(isPaint(arr[x-1][y])){
								markPaint(arr,list,x-1,y);
							}
						}
						
						if(x+1<n){	
							if(isPaint(arr[x+1][y])){
								markPaint(arr,list,x+1,y);
							}
						}
						
						if(y-1>-1){	
							if(isPaint(arr[x][y-1])){
								markPaint(arr,list,x,y-1);
							}
						}
						
						if(y+1<m){	
							if(isPaint(arr[x][y+1])){
								markPaint(arr,list,x,y+1);
							}
						}
					}
					
					if(list.size()>paintArea){
						paintArea =  list.size();
					}
					
					//System.out.println("paintArea ::"+paintArea);
					/*for (int a = 0; a < arr.length; a++) {
						for (int b = 0; b < arr[a].length; b++) {
							System.out.print("["+arr[a][b]+"]");
						}
						System.out.println();
					}
					System.out.println("===================================================");*/
			      
					
				}
				
			
				
				
			}
		}
     
 /*    for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				System.out.print("["+arr[i][j]+"]");
			}
			System.out.println();
		}
   
		System.out.println("paintCount ::"+paintCount);*/
     System.out.println(paintCount);
     System.out.println(paintArea);
		
	}
	
	private static boolean isPaint(int index){
		
		return index==1?true:false;
	}
	
	private static void markPaint(int[][] arr,List<int[]> list,int x,int y){
		int[] indexArray = {x,y};
		arr[x][y]= -1;
		list.add(indexArray);
	}
	
}
