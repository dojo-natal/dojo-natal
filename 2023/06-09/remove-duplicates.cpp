// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int finalCount = 0;
        int count = 0;

        for(int i=0; i< size(nums)-1; i++) {
          if (nums[i] == nums[i+1]) {
            finalCount++;
            if (finalCount >= 2) {
              count++;
            } 
          } else {
            finalCount = 0;
          }
          nums[i]=nums[i+count];
       }
      return size(nums) - count;
    }
};

