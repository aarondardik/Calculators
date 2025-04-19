class Calculator{
    public static int add(int a, int b){
        return a+b;
    }
    public static double add(double a, double b){
        return a + b;
    }
    public static int add(int a, int b, int c){
        return a + b + c;
    }

    public static void main(String[] args){
        int startYear = 2500;
        int endYear = 2024;
        String message = "main pyramids at Giza around.";
        String output = "Egyptians built" + 3 + message + startYear + " " + "BCE and they are still standing in" + endYear + ".";
        System.out.println(output);

        System.out.println("3" + 5 + 2);

        int var1 = 0;
        int var2 = 2;
        while((var2 != 0) && ((var1/var2)>=0)){
            var1 = var1 + 1;
            var2 = var2 - 1;
        }
        System.out.println(String.valueOf(var1));
        System.out.println(String.valueOf(var2));

        String s1 = "Hey";
        String s2 = s1.substring(0, 1);
        String sss = s2.toLowerCase();
        System.out.println(sss);

        String ab1 = "xyz";
        String ab2 = ab1;
        String ab3 = ab2;
        System.out.println(ab1.equals(ab3));
        System.out.println(ab1==ab2);
        System.out.println(ab1 == ab3);

        System.out.println("13" + 5 + 3);


    }
    


}