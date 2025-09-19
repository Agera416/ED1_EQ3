// EMIR ALBERTO PINO MALDONADO

import java.util.Random;

public class VentasTienda {
    static String[] meses = {
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };

    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};

    static Object[][] ventasTienda = new Object[meses.length][departamentos.length];

    public static void main(String[] args) {
        Random rand = new Random();

        // Llenar matriz con ventas aleatorias
        for (int i = 0; i < meses.length; i++) {
            for (int j = 0; j < departamentos.length; j++) {
                ventasTienda[i][j] = rand.nextInt(9501) + 500; // 500 a 10000
            }
        }

        System.out.println("=== VENTAS INICIALES ===");
        imprimirTabla();

        System.out.println("\n--- PRUEBAS DE FUNCIONES ---");
        System.out.println("Venta en Febrero (Deportes): " + buscarVenta(1, 1));

        insertarVenta(2, 2, 9999);
        System.out.println("Nueva venta en Marzo (Juguetería): " + buscarVenta(2, 2));

        eliminarVenta(2, 0);
        System.out.println("Venta eliminada en Marzo (Ropa): " + buscarVenta(2, 0));

        System.out.println("\n=== VENTAS FINALES ===");
        imprimirTabla();
    }

    // Insertar valor en la matriz
    public static void insertarVenta(int mes, int depto, int valor) {
        ventasTienda[mes][depto] = valor;
    }

    // Buscar valor en la matriz
    public static Object buscarVenta(int mes, int depto) {
        return ventasTienda[mes][depto];
    }

    // Eliminar venta (reemplazar con "/////")
    public static void eliminarVenta(int mes, int depto) {
        ventasTienda[mes][depto] = "/////";
    }

    // Imprimir tabla con formato
    public static void imprimirTabla() {
        System.out.printf("%-12s%-12s%-12s%-12s%n", "Mes", "Ropa", "Deportes", "Juguetería");
        for (int i = 0; i < ventasTienda.length; i++) {
            System.out.printf("%-12s", meses[i]);
            for (int j = 0; j < ventasTienda[i].length; j++) {
                System.out.printf("%-12s", ventasTienda[i][j].toString());
            }
            System.out.println();
        }
    }
}
