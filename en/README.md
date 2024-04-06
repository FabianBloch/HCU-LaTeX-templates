# Own commands in LaTeX

In LaTeX you can create your own commands (`\newcommand{}[]{}`) to make your life easier. Here are a few examples that are currently used in the templates:

## Example

```latex
\newcommand{\own}{own command}
```

If you now use `\own` in your document, `own command` is automatically output.

## Use HCU color

```latex
\newcommand{\HCUcolor}[1]{\textcolor{HCU}{#1}}
```

If the text should be displayed in HCU colors:
    
```latex
\HCUcolor{This text is in HCU colors.}
```

## Quotation marks

There are already quotation marks in LaTeX, but they are either not correct or too complicated to write. Therefore there is a separate command for this:

```latex
\newcommand{\Quotationmarks}[1]{\glqq #1\grqq{}}
```

Now if you want to put something in quotation marks:

```latex
\Quotationmarks{This text is enclosed in quotation marks.}
```

## Figure with source

The following function creates a figure with a source. The first parameter is the width of the figure, the second parameter is the file name of the figure, the third parameter is the caption, the fourth parameter is the source and the fifth parameter is the label of the figure.

The width of the figure is set by default to 75% of the text width. If the figure should be narrower or wider, the first parameter can be adjusted.

```latex
\newcommand{\figureWithSource}[5][.75]{
                \begin{figure}[H]
                	\centering
                	\includegraphics[width=#1\textwidth]{Data/#2}
                	\caption{#3}
                	\caption*{Source: #4}
                	\label{fig:#5}
                \end{figure}}
```

If you want to insert a figure with a source:

```latex
\figureWithSource[optional width]{filename}{title}{source}{label addition}

\figureWithSource{filename}{title}{source}{label addition}
```

If you now want to reference the image, this also works as normal (even if overleaf does not suggest this):

```latex
\ref{fig:label addition}
```

## Enumeration with preset distances

You can also use the following command so that you do not always have to specify the spacing of the bullet points:

```latex
\newcommand{\ownItems}[1]{
        \begin{itemize}	
        	\setlength{\itemsep}{-2pt}
        	#1
        \end{itemize}}
```

The following can now be used in the text:

```latex
\ownItems{
    \item First item
    \item Second item
    \item Third item
}
```

## Comment for later editing

To leave comments for later editing, you can create the following command:

```latex
\newcommand{\kommentar}[1]{\textcolor{red1}{\textit{#1}}}
```

This uses the color `red1` and writes the text in italics. If you want to leave a comment:

```latex
\comment{A comment could be written here}.
```

The comments must be removed or commented out <u>**BEFORE SUBMITTING**</u>.

# Closing words

Further own commands will be added here in the future.

Perhaps you can think of a few more useful commands that could be added here.