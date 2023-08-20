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

---

Further own commands will be added here in the future.