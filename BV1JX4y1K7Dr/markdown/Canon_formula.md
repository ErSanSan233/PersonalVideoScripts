此式作废

$$
\begin{align}
&g(x)=\begin{cases}(\boldsymbol G)_{11}, & 0\le x <1\\
(\boldsymbol G)_{k2},&2\le k\le32\quad{\rm s.t.}\;\sum _{i=1}^{k-1}(\boldsymbol G)_{i1} \le x<\sum _{i=1}^{k}(\boldsymbol G)_{i1}\\
0, & \text {否则}\end{cases}\\

&{\text {其中}\;}\boldsymbol G = \left[\begin{matrix}\boldsymbol G_{\rm part-a} \\ \boldsymbol G_{\rm part-b} \\\boldsymbol G_{\rm part-c} \end{matrix}\right]\in \mathbb R ^{32\times 2}{\;\rm 且}\\

&\boldsymbol G_{\rm part-a}=\left[\begin{matrix}
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 2 & 1 & 1 & 2\\
0 & 2 & 4 & 0 & 0 & 2 & 4 & 0 & 4 & 5 & 7 & 4 & 5 & 7 \end{matrix}\right]^{\text T}\in \mathbb R ^{14\times 2},\\

&\boldsymbol G_{\rm part-b}=\left[\begin{matrix}0.5 & 0.5 & 0.5 & 0.5 & 1 & 1 & 0.5 & 0.5 & 0.5 & 0.5 & 1 & 1 \\7 & 9 & 7 & 5 & 4 & 0& 7 & 9 & 7 & 5 & 4 & 0 \end{matrix}\right]^{\text T}\in \mathbb R ^{12\times 2},\\

&\boldsymbol G_{\rm part-c}=\left[\begin{matrix} 1&1&2&1&1&2 \\
2 & -5 & 0 & 2 & -5 & 0\end{matrix}\right]^{\text T}\in \mathbb R ^{6\times 2}.\end{align}
$$

---

# 以此为准

$$
\begin{align}
&g(x)=\begin{cases}

G_{1,2}, & 0\le x < 1\\
G_{k,2}, & k\in\mathbb Z_+,2\le k<32 \quad\text{s.t.}\quad G_{k-1,1}\le x<G_{k,1}\\
0, & \text {否则}\end{cases}\\

&{\text {其中}\;}\boldsymbol G = \left[\begin{matrix}\boldsymbol G_{\rm part-a} \\ \boldsymbol G_{\rm part-b} \\\boldsymbol G_{\rm part-c} \end{matrix}\right]\in \mathbb R ^{32\times 2}{\;\rm 且}\\

&\boldsymbol G_{\rm part-a}=\left[\begin{matrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 12 & 13 & 14 & 16\\
0 & 2 & 4 & 0 & 0 & 2 & 4 & 0 & 4 & 5 & 7 & 4 & 5 & 7 \end{matrix}\right]^{\text T}\in \mathbb R ^{14\times 2},\\

&\boldsymbol G_{\rm part-b}=\left[\begin{matrix}
16.5 & 17 & 17.5 & 18 & 19 & 20 & 20.5 & 21 & 21.5 & 22 & 23 & 24 \\
7 & 9 & 7 & 5 & 4 & 0& 7 & 9 & 7 & 5 & 4 & 0 \end{matrix}\right]^{\text T}\in \mathbb R ^{12\times 2},\\

&\boldsymbol G_{\rm part-c}=\left[\begin{matrix} 
25&26&28 &29&30&32 \\
2 & -5 & 0 & 2 & -5 & 0\end{matrix}\right]^{\text T}\in \mathbb R ^{6\times 2}.\end{align}
$$




$$
f(x)=\begin{cases}4, &x=0\\
2, &x=4\\
1, &x=8\\
\frac{1}{2}, &x=12\\
0, &{\text {否则}}
\end{cases}
$$



$$
(f*g)(x)={\text {同时播放}_{t\in\mathbb R}}(\mathcal D\circ\mathcal V)\left(440\times \left(\sqrt[12]{2}\right)^{ f(t)g(x-t)-9}\right)
$$





