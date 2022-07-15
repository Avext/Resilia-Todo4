dataScientist = {
    'name':[],
    'summary':[],
    }

dataAnalyst = {
    'name':[],
    'summary':[],
    }

nameLS = []
summaryLS = []
keywordsLS = ['python','banco de dados','machine learning','resolução de problemas','estatística']
nameLD = []
summaryLD = []
keywordsLD = ['python','powerbi','sql','boa comunicação']


def insertCandidates():

    candidate = int(input('Digite aqui a quantidade de candidatos a serem inseridos e tecle enter... '))
    if candidate < 1:
        print('Entrada inválida.')
        insertCandidates()

    for i in range (candidate):
        name = input('\nDigite aqui o nome do candidato e tecle enter... ')
        job = int(input('Digite aqui o número referente a vaga para qual o candidato está se inscrevendo e tecle enter \nAnalista de dados(1) ou Cientista de dados(2)... '))
        
        with open('summary'+str(i)+'.txt', 'r',) as archive:
            summary = archive.read()
            summary = summary.lower()

        if job == 1:
            nameLD.append(name)
            summaryLD.append(summary)

        elif job == 2:
            nameLS.append(name)
            summaryLS.append(summary)

        else:
            print('Vaga inválida, nada será inserido!')

    dataScientist.update({'name':nameLS})
    dataScientist.update({'summary':summaryLS})
    dataAnalyst.update({'name':nameLD})
    dataAnalyst.update({'summary':summaryLD})


def queryCandidates():

    print('\nEstá(ão) cadastrado(s) para as vagas de analista de dados',len(dataAnalyst['name']),'candidato(s).')

    countD = 0
    countDT = 0
    for wordD in dataAnalyst['summary']:
        for keywordD in keywordsLD:
            if keywordD in wordD:
                countD = countD + 1
        
        if countD > 0:
            countDT = countDT + 1
        countD = 0
    
    print(countDT,'candidato(s) possuem pelo menos uma das palavras-chave relacionadas à vaga de analista de dados.')


    print('\nEstá(ão) cadastrado(s) para as vagas de cientista de dados',len(dataScientist['name']),'candidato(s).')

    countS = 0 #conta palavras-chave por resumo
    countST = 0 #conta os candidatos que possuem palavras-chave
    for wordS in dataScientist['summary']:
        for keywordS in keywordsLS: #identificar todas as palavras
            if keywordS in wordS:
                countS = countS + 1

        if countS > 0:
            countST = countST + 1
        countS = 0     

    print(countST,'candidato(s) possuem pelo menos uma das palavras-chave relacionadas à vaga de cientista de dados.\n')


insertCandidates()
queryCandidates()