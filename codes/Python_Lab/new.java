class Tortoise extends Thread

{

 public void run()

 {

 int dis = 0;

 

 for(int i=0; i<60; i++)

 {

 if(i%3==0)

 {

 dis += 1;

 System.out.println("Distance covered by Tortoise :: " + dis);

 }

 }

 

 System.out.println("======Tortoise has Completed the race======");

 System.out.println("======Tortoise has Won the race======");

 }

}



class Hare extends Thread

{

 public void run()

 {

 for(int i=1; i<=20; i++)

 {

 System.out.println("Distance covered by Hare :: " + i);

 

 if(i==12)

 {

 System.out.println("Hare has slept.");

 try {

 Thread.sleep(1);

 } catch (InterruptedException e) {

 e.printStackTrace();

 }

 

 System.out.println("Hare woke up.");

 }

 }

 System.out.println("======Hare has completed the race======");

 }

}



public class new extends Thread{

 public static void main(String[] args)

 {

 Hare hare = new Hare();

 Tortoise tortoise = new Tortoise();

 

 hare.start();

 tortoise.start();

 }

}