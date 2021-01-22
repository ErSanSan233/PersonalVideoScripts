

不考虑振动波形和振幅。设振动频率恒定的机械振动集合$\mathbb V$；设音级的集合$\mathbb D$，则有升半音函数、降半音函数满足
$$
(\cdot)♯: \cdot \in \mathbb D \mapsto \cdot + 1 \in \mathbb D,\\
(\cdot)♭:\cdot \in \mathbb D \mapsto \cdot - 1 \in \mathbb D.
$$

设${\mathcal V}: f \in [20, 20000] \mapsto \mathcal V (f) \in \mathbb V$，$\mathcal V (f)$表示振动频率恒为$f$的振动；

设$\mathcal D: v \in \mathbb V \mapsto \mathcal D (v)\in \mathbb D $，$\mathcal D (v)$表示振动$v$的音级；

则可定义中央C，有${\text C}=(\mathcal D\circ\mathcal V)(440)-9\in\mathbb D$；

有
$$
\forall f \in \mathbb R,\quad (\mathcal D\circ\mathcal V)(f) = \log_{\sqrt[12]{2}}(\frac{f}{440}) + \text C + 9.
$$

相应地，有
$$
\forall d \in \mathbb D, \quad {\left(\mathcal V^{-1}\circ\mathcal D^{-1}\right)(\text C+d)}=(\mathcal D\circ\mathcal V)^{-1}(\text C+d)= 440\times(\sqrt[12]{2})^{d-9}.
$$







