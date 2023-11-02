@echo off
REM Clear the temporary files
python .\clear-trash.py

REM Compile the LaTeX document
pdflatex .\index.tex

REM Run BibTeX
bibtex .\index.aux

REM Compile again to incorporate bibliography
pdflatex .\index.tex
pdflatex .\index.tex

REM Clear the temporary files
python .\clear-trash.py

echo Compilation finished. Check the output directory for the PDF.
pause
