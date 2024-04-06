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

## Abbildung mit Quellenangabe

Die folgende Funktion erstellt eine Abbildung mit Quellenangabe. Der erste Parameter ist die Breite der Abbildung, der zweite Parameter ist der Dateiname der Abbildung, der dritte Parameter ist die Bildunterschrift, der vierte Parameter ist die Quelle und der fünfte Parameter ist das Label der Abbildung.

Die Breite der Abbildung ist standardmäßig auf 75% der Textbreite gesetzt. Wenn die Abbildung schmaler oder breiter sein soll, kann der erste Parameter angepasst werden.

```latex
\newcommand{\figureWithSource}[5][.75]{
                \begin{figure}[H]
                	\centering
                	\includegraphics[width=#1\textwidth]{Daten/#2}
                	\caption{#3}
                	\caption*{Quelle: #4}
                	\label{fig:#5}
                \end{figure}}
```

Möchte man nun eine Abbildung mit Quellenangabe einfügen:

```latex
\figureWithSource[optional Breite]{Dateiname}{Titel}{Quellenangabe}{Labelergänzung}

\figureWithSource{Dateiname}{Titel}{Quellenangabe}{Labelergänzung}
```

Möchte man das Bild nun referenzieren, funktioniert das auch ganz normal (auch wenn overleaf das nicht vorschlägt):

```latex
\ref{fig:Labelergänzung}
```

## Aufzählung mit voreingestellten Abständen

Um nicht immer die Abstände der Aufzählungspunkte festzulegen, kann man auch folgenden Befehl verwenden:

```latex
\newcommand{\ownItems}[1]{
        \begin{itemize}	
        	\setlength{\itemsep}{-2pt}
        	#1
        \end{itemize}}
```

Somit kann nun im Text folgendes verwendet werden:

```latex
\ownItems{
    \item Erster Punkt
    \item Zweiter Punkt
    \item Dritter Punkt
}
```

## Kommentar für spätere Bearbeitung

Um Kommentare für spätere Bearbeitung zu hinterlassen, kann man sich folgenden Befehl erstellen:

```latex
\newcommand{\kommentar}[1]{\textcolor{red1}{\textit{#1}}}
```

Dies verwendet die Farbe `red1` und schreibt den Text kursiv. Möchte man somit einen Kommentar hinterlassen:

```latex
\kommentar{Hier könnte ein Kommentar stehen.}
```

Die Kommentare müssen <u>**VOR EINER ABGABE**</u> entfernt oder auskommentiert werden.

# Schlusswort

Weitere eigene Befehle werden in Zukunft hier ergänzt.

Vielleicht fallen euch ja auch noch ein paar nützliche Befehle ein, die hier ergänzt werden könnten.