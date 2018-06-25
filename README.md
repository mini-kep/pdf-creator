# pdf-creator
Experimental PDF output with Cyrillic letters

#### Possible pipelines:
 - `html -> pdf` (no precise formatting, but easy to setup; has errors with cyrillic letters)  
 - `reportlab -> pdf` (errors with cyrillic letters) 
 - `docx template -> pdf` (with <https://github.com/elapouya/python-docx-template>)
 - `latex - > pdf` (latex installation too heavy and template too complex, but very precise)
 - scientific writing with [pweave](mpastell.com/pweave/) (linear text only)
 - plotly html report generation 
    
#### References:
 - [Three ways to make a PDF from HTML in Python](https://gist.github.com/philfreo/44e2e26a65820497db234d0c66ed58ae)

#### Current task (2018-06-25):

Make Russian fonts work in reportlab/xhtml2pdf

  - https://stackoverflow.com/questions/34158693/xhtml2pdf-cyrillic-characters-dont-work
  - http://code.activestate.com/recipes/438817-how-to-use-cyrillic-fonts-in-reportlab-pdf-library/    
    


