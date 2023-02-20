public class thread_demo {
    public static void main(String[] args) {
        Thread tortoise = new Tortoise(); // Creating an object of the tortoise thread
        tortoise.start(); // Starting the first thread
        for (int a = 1; a < 11; a++) {
            System.out.println("Distance covered by HARE   = " + (a));
        }

        System.out.println("!!!!!!!!!!!!!!!HARE IS GOING TO SLEEP!!!!!!!!!!!!!!!!!!!!!"); // hare going to sleep

        try {
            Thread.sleep(3000); // current thread is hare
        }

        catch (InterruptedException e) {

        }

        System.out.println("!!!!!!!!!!!!!!HARE AGAIN STARTED THE RACE !!!!!!!!!!!!!!!!"); // hare wakes up

        for (int b = 11; b < 21; b++)
            System.out.println("Distance covered by HARE   = " + (b));

        System.out.println("!!!!!!!!!!!!!!!!!!!!HARE HAS COMPLETED THE RACE !!!!!!!!!!!!!!!!!!!");
    }

}