http://tex.stackexchange.com/questions/66109/aligning-a-figure-and-table-side-by-side
```tex
% \usepackage[export]{adjustbox}
```

```tex
\pagebreak
\begin{minipage}[t]{.25\linewidth}
  \vspace{0pt}
  \centering
  \includegraphics[scale=0.5]{emissions_10.png}
\end{minipage}
\begin{minipage}[t]{.25\linewidth}
  \vspace{0pt}
  \centering
  \begin{tabular}{l}
  \includegraphics[width=5cm]{CEMT_40_10_overlap.png}
  \includegraphics[width=5cm]{CEMT_42_10_overlap.png}
  \includegraphics[width=5cm]{CEMT_44_10_overlap.png}\\
  \includegraphics[width=5cm]{CEMT_41_10_overlap.png}
  \includegraphics[width=5cm]{CEMT_43_10_overlap.png}
  \includegraphics[width=5cm]{CEMT_45_10_overlap.png}\\
  \end{tabular}
\end{minipage}
```
