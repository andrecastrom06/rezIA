import pyttsx3
import datetime
import locale

while True:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        hoje = datetime.date.today()
        dia_semana = hoje.strftime('%A').lower()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150) 
        engine.setProperty('volume', 1)

        painosso = "Pai nosso que estais no céu, santificado seja o vosso nome. Venha a nós o vosso reino. Seja feita a vossa vontade, assim na terra como no céu. O pão nosso de cada dia nos dai hoje. Perdoai as nossas ofensas, assim como nós perdoamos a quem nos tem ofendido. E não nos deixeis cair em tentação, mas livrai-nos do mal. Amém."  
        avemaria = "Ave Maria, cheia de graça, o Senhor é convosco. Bendita sois vós entre as mulheres e bendito é o fruto do vosso ventre, Jesus. Santa Maria, Mãe de Deus, rogai por nós pecadores, agora e na hora de nossa morte. Amém."
        santoanjo = "Santo Anjo do Senhor, meu zeloso guardador, se a ti me confiou a piedade divina, sempre me rege, me guarda, me governa e ilumina. Amém."
        salverainha = "Salve Rainha, Mãe de misericórdia, vida, doçura e esperança nossa, salve! A vós bradamos os degredados filhos de Eva. A vós suspiramos, gemendo e chorando neste vale de lágrimas. Eia, pois, advogada nossa, esses vossos olhos misericordiosos a nós volvei. E depois deste desterro, mostrai-nos Jesus, bendito fruto do vosso ventre. Ó clemente! Ó piedosa! Ó doce Virgem Maria! Rogai por nós, Santa Mãe de Deus, para que sejamos dignos das promessas de Cristo. Amém."
        oferecimentoTerco = "Divino Jesus, Nós Vos oferecemos este Terço que vamos rezar, Meditando nos mistérios da Vossa Redenção. Concedei-nos, Por intercessão da Virgem Maria, Mãe de Deus e nossa Mãe, As virtudes que nos são necessárias Para bem rezá-lo E a graça de ganharmos as indulgências Desta santa devoção."
        oferecimentoRosario = "Divino Jesus, Nós Vos oferecemos este Rosário que vamos rezar, Meditando nos mistérios da Vossa Redenção. Concedei-nos, Por intercessão da Virgem Maria, Mãe de Deus e nossa Mãe, As virtudes que nos são necessárias Para bem rezá-lo E a graça de ganharmos as indulgências Desta santa devoção."
        credo = "Creio em Deus Pai todo poderoso, Criador do céu e da terra, e em Jesus Cristo, seu único Filho, nosso Senhor, que foi concebido pelo poder do Espírito Santo; nasceu da Virgem Maria; padeceu sob Pôncio Pilatos; foi crucificado, morto e sepultado; desceu à mansão dos mortos; ressuscitou ao terceiro dia; subiu aos céus; está sentado à direita de Deus Pai todo poderoso, donde há de vir a julgar os vivos e os mortos. Creio no Espírito Santo; na Santa Igreja Católica; na comunhão dos santos; na remissão dos pecados; na ressurreição da carne; na vida eterna. Amém."
        m1gozosos = "primeiro mistério gozoso. A anunciação do Anjo à Virgem Maria."
        m2gozosos = "segundo mistério gozoso. A visitação de Nossa Senhora à sua prima Isabel."
        m3gozosos = "terceiro mistério gozoso. O nascimento de Jesus em Belem."
        m4gozosos = "quarto mistério gozoso. A apresentação do Menino Jesus no templo."
        m5gozosos = "quinto mistério gozoso. A perda e o encontro do Menino Jesus no templo."
        m1luminosos = "primeiro mistério luminoso. O batismo de Jesus no rio Jordão."
        m2luminosos = "segundo mistério luminoso. A auto-revelação de Jesus nas bodas de Caná."
        m3luminosos = "terceiro mistério luminoso. O anúncio do Reino de Deus e o convite à conversão."
        m4luminosos = "quarto mistério luminoso. A transfiguração de Jesus no monte tabor."
        m5luminosos = "quinto mistério luminoso. A instituição da Eucaristia."
        m1dolorosos = "primeiro mistério doloroso. A oração de Jesus no Horto das Oliveiras."
        m2dolorosos = "segundo mistério doloroso. A flagelação de Jesus preso à coluna."
        m3dolorosos = "terceiro mistério doloroso. A coroação de espinhos."
        m4dolorosos = "quarto mistério doloroso. Jesus carregando a cruz até o Calvário."
        m5dolorosos = "quinto mistério doloroso. A crucificação e morte de Jesus."
        m1gloriosos = "primeiro mistério glorioso. A ressurreição de Jesus."
        m2gloriosos = "segundo mistério glorioso. A ascensão de Jesus ao céu."
        m3gloriosos = "terceiro mistério glorioso. A vinda do Espírito Santo sobre os apóstolos."
        m4gloriosos = "quarto mistério glorioso. A assunção de Nossa Senhora ao céu."
        m5gloriosos = "quinto mistério glorioso. A coroação de Nossa Senhora como Rainha do céu e da terra."
        oMeuJesus = "Ó meu Jesus, perdoai-nos, livrai-nos do fogo do inferno, levai as almas todas para o céu e socorrei principalmente as que mais precisarem da vossa misericórdia."
        gloria = "Glória ao Pai, ao Filho e ao Espírito Santo, como era no princípio, agora e sempre. Amém."
        preparacaoSalveRainha = "Infinitas graças vos damos soberana Rainha, pelos beneficios que todos os dias recebemos de vossas mãos liberais, dignai-vos agora e para sempre, tomar-nos debaixo do vosso poderoso amparo, e para mais vos alegrar vos saudamos com a Salve Rainha."
        tercosegsab = "Mistério gozoso"
        tercoqui = "Mistério luminoso"
        tercotersex = "Mistério doloroso"
        tercoquadom = "Mistério glorioso"
        introdutorio = "Em nome do Pai, do Filho e do Espírito Santo. Amém"

        oracao = int(input("Escolha uma opção:\n1 - Rezar o terço\n2 - Rezar o Rosário\n3 - Rezar o pai nosso\n4 - Rezar a ave maria\n5 - Rezar o Santo Anjo\n--> "))

        def rezar_misterio(nome, engine):
            engine.say(nome)
            engine.runAndWait()
            engine.say(painosso)
            engine.runAndWait()
            for _ in range(10):
                engine.say(avemaria)
                engine.runAndWait()
            engine.say(gloria)
            engine.runAndWait()
            engine.say(oMeuJesus)
            engine.runAndWait()

        if oracao == 1:
            escolha = "Então rezaremos o terço"
            engine.say(escolha)
            engine.runAndWait()
            engine.say(oferecimentoTerco)
            engine.runAndWait()
            engine.say(introdutorio)
            engine.runAndWait()
            engine.say(credo)
            engine.runAndWait()

            if dia_semana == "segunda-feira" or dia_semana == "sábado":
                engine.say(tercosegsab)
                engine.runAndWait()
                rezar_misterio(m1gozosos, engine)
                rezar_misterio(m2gozosos, engine)
                rezar_misterio(m3gozosos, engine)
                rezar_misterio(m4gozosos, engine)
                rezar_misterio(m5gozosos, engine)

            elif dia_semana == "quinta-feira":
                engine.say(tercoqui)
                engine.runAndWait()
                rezar_misterio(m1luminosos, engine)
                rezar_misterio(m2luminosos, engine)
                rezar_misterio(m3luminosos, engine)
                rezar_misterio(m4luminosos, engine)
                rezar_misterio(m5luminosos, engine)

            elif dia_semana == "terça-feira" or dia_semana == "sexta-feira":
                engine.say(tercotersex)
                engine.runAndWait()
                rezar_misterio(m1dolorosos, engine)
                rezar_misterio(m2dolorosos, engine)
                rezar_misterio(m3dolorosos, engine)
                rezar_misterio(m4dolorosos, engine)
                rezar_misterio(m5dolorosos, engine)

            elif dia_semana == "quarta-feira" or dia_semana == "domingo":
                engine.say(tercoquadom)
                engine.runAndWait()
                rezar_misterio(m1gloriosos, engine)
                rezar_misterio(m2gloriosos, engine)
                rezar_misterio(m3gloriosos, engine)
                rezar_misterio(m4gloriosos, engine)
                rezar_misterio(m5gloriosos, engine)
            
            engine.say(preparacaoSalveRainha)
            engine.runAndWait()
            engine.say(salverainha)
            engine.runAndWait()
            engine.say(introdutorio)
            engine.runAndWait()

        elif oracao == 2:
            escolha = "Então rezaremos o rosário"
            engine.say(escolha)
            engine.runAndWait()
            engine.say(oferecimentoRosario)
            engine.runAndWait()
            engine.say(introdutorio)
            engine.runAndWait()
            engine.say(credo)
            engine.runAndWait()

            engine.say(tercosegsab)
            engine.runAndWait()
            
            rezar_misterio(m1gozosos, engine)
            rezar_misterio(m2gozosos, engine)
            rezar_misterio(m3gozosos, engine)
            rezar_misterio(m4gozosos, engine)
            rezar_misterio(m5gozosos, engine)

            engine.say(tercoqui)
            engine.runAndWait()
            
            rezar_misterio(m1luminosos, engine)
            rezar_misterio(m2luminosos, engine)
            rezar_misterio(m3luminosos, engine)
            rezar_misterio(m4luminosos, engine)
            rezar_misterio(m5luminosos, engine)

            engine.say(tercotersex)
            engine.runAndWait()
            
            rezar_misterio(m1dolorosos, engine)
            rezar_misterio(m2dolorosos, engine)
            rezar_misterio(m3dolorosos, engine)
            rezar_misterio(m4dolorosos, engine)
            rezar_misterio(m5dolorosos, engine)
            
            engine.say(tercoquadom)
            engine.runAndWait()
            
            rezar_misterio(m1gloriosos, engine)
            rezar_misterio(m2gloriosos, engine)
            rezar_misterio(m3gloriosos, engine)
            rezar_misterio(m4gloriosos, engine)
            rezar_misterio(m5gloriosos, engine)

            engine.say(preparacaoSalveRainha)
            engine.runAndWait()
            engine.say(salverainha)
            engine.runAndWait()
            engine.say(introdutorio)
            engine.runAndWait()

        elif oracao == 3:
            escolha = "Então rezaremos o pai nosso"
            engine.say(escolha)
            engine.runAndWait()
            engine.say(painosso)
            engine.runAndWait()

        elif oracao == 4:
            escolha = "Então rezaremos a ave maria"
            engine.say(escolha)
            engine.runAndWait()
            engine.say(avemaria)
            engine.runAndWait()

        elif oracao == 5:
            escolha = "Então rezaremos o Santo Anjo"
            engine.say(escolha)
            engine.runAndWait()
            engine.say(santoanjo)
            engine.runAndWait()

    except Exception as e:
        print(f"Erro: {e}. Reiniciando o programa.")
        continue