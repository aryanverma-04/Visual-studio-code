public class thread_demo {
    public static void main(String[] args) {
        System.out.println("\n\nName: Aryan verma, UID: 20bcs3651\n");
        Thread tortoise = new Tortoise();
        tortoise.start(); 
        for (int a = 1; a < 11; a++) {
            System.out.println("Distance covered by HARE   = " + (a));
        }

        System.out.println("!!!!!!!!!!!!!!!HARE IS GOING TO SLEEP!!!!!!!!!!!!!!!!!!!!!");

        try {
            Thread.sleep(3000); 

        catch (InterruptedException e) {

        }

        System.out.println("!!!!!!!!!!!!!!HARE AGAIN STARTED THE RACE !!!!!!!!!!!!!!!!"); 

        for (int b = 11; b < 21; b++)
            System.out.println("Distance covered by HARE   = " + (b));

        System.out.println("!!!!!!!!!!!!!!!!!!!!HARE HAS COMPLETED THE RACE !!!!!!!!!!!!!!!!!!!");
    }

}

class Tortoise extends Thread {
    public void run() {
        for (int c = 1; c < 21; c++) {
            System.out.println("Distance covered by TORTOISE = " + c);
        }

        System.out.println("!!!!!!!!!!!!!!!!TORTOISE HAS WON THE RACE !!!!!!!!!!!!!!!!!!!!!"); 

    }
}
