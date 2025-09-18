// EMIR ALBERTO PINO MALDONADO

import java.util.Random;

public class CalificacionesAlumnos {
    public static void main(String[] args) {
        Random random = new Random(0); // Semilla fija para reproducibilidad

        int[][] alumnos = new int[500][6];

        // Generar calificaciones aleatorias entre 50 y 100
        for (int i = 0; i < 500; i++) {
            for (int j = 0; j < 6; j++) {
                alumnos[i][j] = random.nextInt(51) + 50; // 50 a 100
            }
        }

        long startTime = System.nanoTime();

        int alumnoNum = 321;
        int materiaNum = 6;

        int calificacion = alumnos[alumnoNum - 1][materiaNum - 1];

        // Imprimir encabezados
        System.out.printf("%-10s", "Alumno");
        for (int j = 1; j <= 6; j++) {
            System.out.printf("Materia %-8d", j);
        }
        System.out.println();

        // Imprimir calificaciones
        for (int i = 0; i < alumnos.length; i++) {
            System.out.printf("%-10d", i + 1);
            for (int j = 0; j < alumnos[i].length; j++) {
                System.out.printf("%-12d", alumnos[i][j]);
            }
            System.out.println();
        }

        long endTime = System.nanoTime();
        double elapsedSeconds = (endTime - startTime) / 1_000_000_000.0;

        System.out.printf("\nLa calificación del alumno No.%d en la materia %d: %d\n", alumnoNum, materiaNum, calificacion);
        System.out.printf("Tiempo de ejecución: %.10f segundos\n", elapsedSeconds);
    }
}
