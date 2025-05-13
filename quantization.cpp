/*
 *	 	 .... In the name of ALLAH ..... 	
 *  	 	 Bismillahir Rahmanir Rahim 	
 */
 
/*
 * @author : Me
 * created : 2025-05-13 19:28:55
 * filename: test.cpp
 */
 
#include <bits/stdc++.h>
using namespace std;
/// type define part
typedef long long ll;
typedef double dl;
/// define Part
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);
#define PB push_back
#define F first
#define S second
#define MP make_pair
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(x) (int)x.size()
#define mem(a, b) memset(a, b, sizeof(a))
#define lower(s) transform(s.begin(), s.end(), s.begin(), ::tolower);
#define upper(s) transform(s.begin(), s.end(), s.begin(), ::toupper);
#define MOD 1000000007
#define fraction(a) \
    cout << fixed;  \
    cout << setprecision(a);
#define debug(x)         \
    cout << #x << " = "; \
    _print(x);           \
    cout << endl;
/// value
const double PI = acos(-1);
const double eps = 1e-9;
const int inf = 2000000000;
const ll infLL = 9000000000000000000;
 
bool sortbysec(const pair<int, int> &a, const pair<int, int> &b) { return (a.second < b.second); }
template <class T>
void _print(T x) { cout << x; }
template <class T>
void _print(vector<T> x)
{
    cout << "[ ";
    for (T i : x)
        cout << i << " ";
    cout << "]";
}
template <class T>
void _print(set<T> x)
{
    cout << "[ ";
    for (T i : x)
        cout << i << " ";
    cout << "]";
}
template <class T, class V>
void _print(pair<T, V> x) { cout << "{" << x.first << "," << x.second << "} "; }
template <class T, class V>
void _print(map<T, V> x)
{
    cout << "[ ";
    for (auto i : x)
        _print(i);
    cout << "]";
}
template <class T>
void _print(multiset<T> x)
{
    cout << "[ ";
    for (T i : x)
        cout << i << " ";
    cout << "]";
}

int main()
{
    fast();
    int rows , cols;
    cout << "Enter the value of rows and cols" <<endl;
    cin >> rows >> cols;

    int image[rows][cols];

    cout << "Enter the 2x2 image pixel values (0–255):\n";
    for(int i = 0; i < rows; i++){
        for(int j = 0 ; j < cols; j++){
            cin >> image[i][j];
        }
    }

    int k;
    cout << "Enter the value of k (e.g., 5 for 2^5 = 32 gray levels): "<< endl;
    cin >> k;

    int bitsToClear = 8 - k;

    int mask = 0xFF << bitsToClear;

    int quantized[rows][cols];

    cout << "Quantized Images: " << endl;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            quantized[i][j] = image[i][j] & mask;
            cout << quantized[i][j] << "\t";
        }
        cout << endl;
    }


    return 0;
}