ll mod = 1000000007;
const int N = 10; //Change Here
ll f[N], invf[N];
int dp[N][N][N / 2 + 10];

ll mpow(ll x, ll y) {
	ll res = 1;
	x = x % mod;
	while (y > 0) {
		if (y & 1) res = (res * x) % mod;
		y = y >> 1;
		x = (x * x) % mod;
	}
	return res;
}

ll modInv(ll n) {
	return mpow(n, mod - 2);
}

ll C(ll n, ll r) {
	if (r == 0) return 1;
	assert(n >= r);
	return (f[n] * invf[r] % mod * invf[n - r] % mod) % mod;
}

void fact() {
	f[0] = 1;
	invf[0] = 1;
	for (int i = 1; i < N; i++) {
		f[i] = (f[i - 1] * i) % mod;
		invf[i] = modInv(f[i]);
	}
}
