import java.util.Arrays;

public class TwoSum {

    public static void main(String[] args) {
      int[] nums = {2, 7, 11, 15};
      int target = 9;

      System.out.println(Arrays.toString(TwoSum.twoSum(nums, target)));
    }

    public static int[] twoSum(int[] nums, int target) {

      int[] retVal = new int[2];

      for (int i = 0; i < nums.length - 1; i ++) {
        for (int j = nums.length - 1; j >= 0; j--) {
          if (nums[i] + nums[j] == target) {
            retVal[1] = i;
            retVal[0] = j;
          }
        }
      }
      return retVal;
    }
}
