TEXFILE= tesisEguinoa
DIR=.

TEXFILES=$(wildcard $(DIR)/*.tex)

all: $(TEXFILE).pdf
 
 
# Compile main tex file and show errors
$(TEXFILE).pdf: $(TEXFILES) 
	pdflatex -pdf -quiet $(TEXFILE)

clean:
	rm -fv *.aux *.log *.toc *.blg *.bbl *.synctex.gz
	rm -fv *.out *.bcf *blx.bib *.run.xml
