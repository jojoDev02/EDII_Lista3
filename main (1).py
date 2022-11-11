class No:

    def __init__(no, chave):
        no.chave = chave
        no.esq = None
        no.dir = None

    def insere(no, chave):
        # chave do nó filho é menor que do nó pai
        if chave < no.chave:
            if no.esq:
                no.esq.insere(chave)
            else:
                no.esq = No(chave)
                return
        # chave do nó filho é maior que do nó pai 
        else:
            if no.dir:
                no.dir.insere(chave)
            else:
                no.dir = No(chave)
                return

    def insereIterativo(no, chave):

        while():
            #se o nó é maior que a chave
            while(no.chave > chave):
                if(no.esq == None):
                    no.esq = No(chave)
                    return
                no = no.esq

            #se o nó é menor que a chave
            while(no.chave < chave):
                if(no.dir == None):
                    no.dir = No(chave)
                    return
                no = no.dir
        
    def busca(no, chave):
    
        # a chave não se encotra na arvore
        if (no == None):
            return None
        # deve ir para esquerda
        if (no.chave > chave):
            no.esq.busca(chave)
        # deve ir para a direita
        else:
            if (no.chave < chave):
                no.dir.busca(chave)
            # chave encontrada
            else:
                return no.chave


