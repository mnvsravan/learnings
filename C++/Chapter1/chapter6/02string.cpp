#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int main() {

    string s = "Hello";
    string s2 = "World";

    // 1. length() / size()
    cout << "Length : " << s.length() << endl;
    cout << "Size   : " << s.size() << endl;

    // 2. empty()
    cout << "Empty? : " << s.empty() << endl;

    // 3. append()
    s.append(" C++");
    cout << "append() : " << s << endl;

    // 4. push_back()
    s.push_back('!');
    cout << "push_back() : " << s << endl;

    // 5. pop_back()
    s.pop_back();
    cout << "pop_back() : " << s << endl;

    // 6. substr()
    cout << "substr(6,3) : " << s.substr(6,3) << endl;

    // 7. find()
    cout << "find(\"C++\") : " << s.find("C++") << endl;

    // 8. erase()
    string temp = s;
    temp.erase(5,4);
    cout << "erase() : " << temp << endl;

    // 9. insert()
    temp.insert(5," Everyone");
    cout << "insert() : " << temp << endl;

    // 10. replace()
    temp.replace(6,8,"Friend");
    cout << "replace() : " << temp << endl;

    // 11. compare()
    cout << "compare() : " << s.compare(s2) << endl;

    // 12. clear()
    string str = "Programming";
    str.clear();
    cout << "clear() Length : " << str.length() << endl;

    // 13. at()
    cout << "at(1) : " << s.at(1) << endl;

    // 14. front() and back()
    cout << "front() : " << s.front() << endl;
    cout << "back()  : " << s.back() << endl;

    // 15. swap()
    cout << "Before Swap : " << s << " " << s2 << endl;
    s.swap(s2);
    cout << "After Swap  : " << s << " " << s2 << endl;

    // 16. resize()
    s.resize(3);
    cout << "resize(3) : " << s << endl;

    // 17. reverse()
    string rev = "Programming";
    reverse(rev.begin(), rev.end());
    cout << "reverse() : " << rev << endl;

    // 18. sort()
    string sortStr = "dcabfe";
    sort(sortStr.begin(), sortStr.end());
    cout << "sort() : " << sortStr << endl;

    // 19. toupper()
    string upper = "hello";
    for(char &c : upper)
        c = toupper(c);
    cout << "toupper() : " << upper << endl;

    // 20. tolower()
    string lower = "HELLO";
    for(char &c : lower)
        c = tolower(c);
    cout << "tolower() : " << lower << endl;

    return 0;
}