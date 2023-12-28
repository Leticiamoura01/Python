from docx import Document
from docx.shared import Pt

#Abri o arquivo do word
arquivoWord = Document("C:\\Users\kauan\Downloads\\1 rpa\python\\pythonProject1\\Word\\Certificado1.docx")

#seleciona o estilo
estilo = arquivoWord.styles["Normal"]

#for = para
for paragrafo in arquivoWord.paragraphs:

    #if = se
    if "@nome" in paragrafo.text:
        paragrafo.text = "Briana Queiroz"
        fonte = estilo.font
        fonte.name = "Calibri (Corpo)"
        fonte.size = Pt(24)


#salvando o certificado do aluno
arquivoWord.save("Briana Queiroz.docx")

