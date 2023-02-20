public class final2 extends Thread {
    public void run() {
        System.out.println("Thread is running by extending the Thread class.");
    }

    public static void main(String args[]) {
        System.out.println("\nName: Aryan verma, Uid: 20bcs3651\n");
        final2 t1 = new final2();
        t1.start();
    }
}
