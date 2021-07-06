class Task1{
    static final int NUM = 1000;
    public static void main(String[] args) {
        long numbers = 0;
        long sum = 0;
        int counter = 0;
        while (counter!=NUM){
            if(isPrimeNumber(numbers)) {
                counter++;
                sum += numbers;
            }
            numbers++;
        }

        System.out.println("Sum: " + sum);
    }

    static boolean isPrimeNumber(long number){
        if(number==0 || number==1)
            return false;
        else
            for(int i=2; i<=Math.sqrt(number); i++)
                if(number%i==0)
                    return false;
        return true;
    }

}