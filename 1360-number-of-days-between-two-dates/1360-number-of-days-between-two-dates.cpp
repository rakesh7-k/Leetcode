class Solution {
public:
    bool leap_year(int y) {
        return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
    }

    int daysFromBase(string date) {
        vector<int> months = {31,28,31,30,31,30,31,31,30,31,30,31};

        int y = stoi(date.substr(0,4));
        int m = stoi(date.substr(5,2));
        int d = stoi(date.substr(8,2));

        int total = 0;

        for (int i = 1971; i < y; i++) {
            total += leap_year(i) ? 366 : 365;
        }

        for (int i = 1; i < m; i++) {
            total += months[i-1];
            if (i == 2 && leap_year(y)) total++;
        }

        total += d;

        return total;
    }

    int daysBetweenDates(string date1, string date2) {
        return abs(daysFromBase(date1) - daysFromBase(date2));
    }
};