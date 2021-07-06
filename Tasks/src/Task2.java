import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task2 {

    public static void main(String[] args) {

        int given_array [] = {2,3,6,6,8,9,10,10,10,12,12};

        int result_arr [] = Arrays.stream(given_array).distinct().toArray();
        System.out.println("First way");
        for(int i: result_arr)
            System.out.print(i + " ");

        System.out.println("\nSecond way");
        int result_arr2 [] = removeDuplicates(given_array);

        for(int i: result_arr2)
            System.out.print(i + " ");

    }


    static int [] removeDuplicates(int arr []) {
        List<Integer> result = new ArrayList<>();
        if (arr.length == 0 || arr.length == 1)
            return arr;

        for (int i = 0; i < arr.length - 1; i++)
            if (arr[i] != arr[i + 1])
                result.add(arr[i]);
        result.add(arr[arr.length-1]);

        return result.stream().mapToInt(i->i).toArray();
    }



}
