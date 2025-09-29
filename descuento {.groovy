DescuentoCompras {

    // Función con valor predeterminado
    public static double calcular_descuento(double montoTotal, double porcentajeDescuento) {
        return montoTotal * (porcentajeDescuento / 100);
    }

    // Sobrecarga para usar el valor por defecto (10%)
    public static double calcular_descuento(double montoTotal) {
        return calcular_descuento(montoTotal, 10); // 10% por defecto
    }

    public static void main(String[] args) {
        double compra1 = 100.0; 
        double compra2 = 200.0;

        // 1. Usando el valor por defecto (10%)
        double descuento1 = calcular_descuento(compra1);
        double total1 = compra1 - descuento1;
        System.out.println("Compra: $" + compra1);
        System.out.println("Descuento: $" + descuento1);
        System.out.println("Total a pagar: $" + total1);

        // 2. Usando un porcentaje personalizado (20%)
        double descuento2 = calcular_descuento(compra2, 20);
        double total2 = compra2 - descuento2;
        System.out.println("\nCompra: $" + compra2);
        System.out.println("Descuento: $" + descuento2);
        System.out.println("Total a pagar: $" + total2);
    }
}
