public class Task3 {

    public static void main(String[] args) {

        String text = "Tiger Runs @ The Speed Of 100 km/hour.";
        int uppercase = 0;
        int lowercase = 0;
        int digit = 0;
        int special = 0;

        for(int i = 0; i<text.length(); i++){
            if(Character.isUpperCase(text.charAt(i)))
                uppercase++;
            else if(Character.isLowerCase(text.charAt(i)))
                lowercase++;
            else if(Character.isDigit(text.charAt(i)))
                digit++;
            else
                special++;
        }

        if (uppercase != 0)
            System.out.printf("Number of uppercase letters is %d. So percentage is %.2f%%\n", uppercase, uppercase*1.0/text.length()*100);
        else
            System.out.println("Number of uppercase letters is 0. So percentage is 0%");

        if (lowercase != 0)
            System.out.printf("Number of lowercase letters is %d. So percentage is %.2f%%\n", lowercase, lowercase*1.0/text.length()*100);
        else
            System.out.println("Number of lowercase letters is 0. So percentage is 0%");


        if (digit != 0)
            System.out.printf("Number of digit letters is %d. So percentage is %.2f%%\n", digit, digit*1.0/text.length()*100);
        else
            System.out.println("Number of digit letters is 0. So percentage is 0%");


        if (special != 0)
            System.out.printf("Number of special letters is %d. So percentage is %.2f%%\n", special, special*1.0/text.length()*100);
        else
            System.out.println("Number of special letters is 0. So percentage is 0%");

    }
}

