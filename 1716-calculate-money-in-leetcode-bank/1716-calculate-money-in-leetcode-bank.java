class Solution {
    public int totalMoney(int n) {
      //  arithmetic Sn​=n/2​[2a+(n−1)d]
  int weeks=n/7;
  int days=n%7;
          int fullWeeks = weeks * (28 + 28 + 7 * (weeks - 1)) / 2;

  int remaining = days * (2 * weeks + days + 1) / 2;

        return fullWeeks + remaining;
      }
}