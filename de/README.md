# Eigene Befehle in LaTeX

In LaTeX kann man eigene Befehle (`\newcommand{}[]{}`) erstellen, um sich das Leben zu erleichtern. Hier ein paar Beispiele, die aktuell in den Vorlagen verwendet werden:

## Beispiel

```latex
\newcommand{\eigener}{eigener Befehl}
```

Wenn man nun `\eigener` in seinem Dokument verwendet, wird automatisch `eigener Befehl` ausgegeben.

## HCU-Farbe verwenden

```latex
\newcommand{\HCUcolor}[1]{\textcolor{HCU}{#1}}
```

Wenn der Text in HCU-Farben dargestellt werden soll:
    
```latex
\HCUcolor{Dieser Text ist in HCU-Farben.}
```

## Anführungszeichen

Es gibt zwar auch schon Anführungszeichen in LaTeX, aber diese sind entweder nicht korrekt oder zu kompliziert zu schreiben. Deshalb gibt es hierfür einen eigenen Befehl:

```latex
\newcommand{\Quotationmarks}[1]{\glqq #1\grqq{}}
```

Soll nun was in Anführungszeichen gesetzt werden:

```latex
\Quotationmarks{Dieser Text steht in Anführungszeichen.}
```

---

Weitere eigene Befehle werden in Zukunft hier ergänzt.