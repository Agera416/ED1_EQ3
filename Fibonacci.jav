// EMIR ALBERTO PINO MALDONADO
// Programa para imprimir la serie de Fibonacci hasta 1 millón de términos en Java

import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("¿Cuántos términos de la serie de Fibonacci deseas imprimir? (máximo 1,000,000): ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Por favor, ingresa un número mayor que 0.");
        } else {
            long a = 0, b = 1;
            for (int i = 0; i < n; i++) {
                System.out.println(a);
                long temp = a + b;
                a = b;
                b = temp;
            }
        }

        sc.close();
    }
}
