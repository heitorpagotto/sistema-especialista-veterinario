from data import animals, animalBreeds, nutritions, vaccineCycles, symptoms, illnesses, medications
from data import Animal, AnimalBreed, ENutritionQuantityType, Illness
from typing import List

# define se o programa deve continuar rodando ou não
shouldProgramRun = True
# define uma variável global da classe Animal
animalObj: Animal = None
# define uma variável global da classe AnimalBreed
breedObj: AnimalBreed = None
# define uma variável global do tipo float para guardar o peso informado do animal
animalWeight: float = 0.00


# definição de classe para formatação na hora de imprimir informações na tela
class ANSI:
    END = '\033[0m' # finalização da linha
    BOLD = '\033[1m' # deixa texto em negrito
    UNDERLINE = '\033[4m' # deixa texto com uma linha


# Função que traz uma string concatenada com o nome dos sintomas, baseado em uma lista de ids de sintomas
def _getIllnessSymptoms(symptomsId: List[int]):
    allSymptoms: List[str] = []
    for pos, symptomId in enumerate(symptomsId):
        for symptom in symptoms:
            if symptom.id == symptomId:
                allSymptoms.insert(pos, symptom.name)

    return ','.join(allSymptoms)


# Função que traz uma string concatenada com o nome dos tratamentos pra uma doença, baseado em uma lista de ids de
# remédios
def _getIllnessTreatments(medicationIds: List[int]):
    allMedications: List[str] = []
    for pos, medicationId in enumerate(medicationIds):
        for medication in medications:
            if medication.id == medicationId:
                allMedications.insert(pos, medication.name)

    return ','.join(allMedications)


# Função que calcula média ponderada baseada em um objeto de doença, olhando a intensidade dos sintomas na doença
# informada
def _calculateMedium(ill: Illness):
    total = sum(s.symptomIntensity for s in ill.symptoms)
    return float(ill.occurrences) / total * 100


# Função que imprime as possíveis doenças que um animal pode ter
def _printPossibleIllness():
    # Sintomas são informados separados por vírgula. Ex: Febre,Tosse
    symptomString = input("\nInforme os sintomas do animal separados por vírgula (não informe nada para retornar)\n")
    symptomSplit = symptomString.split(",")

    if len(symptomSplit) == 0:
        return

    # É realizado uma busca para os sintomas informados, salvando para um filtro futuro
    allSymptoms = []
    for splitted in symptomSplit:
        for symptom in symptoms:
            if symptom.name == splitted:
                allSymptoms.append(symptom)
                break

    print("Seguem algumas potenciais doenças de acordo com os sintomas informados:\n")

    # É realizado um filtro para a busca de doenças de acondo com os sintomar informados
    illnessToPrint = []
    for illness in illnesses:
        for sym in allSymptoms:
            for element in illness.symptoms:
                # Além de filtrar pelo id do sintoma informado, é filtrado pelo id do animal informado
                # evitando doenças que não são possíveis de ocorrer em uma espécie especifica
                # É feito um outro filtro para evitar que doenças já existentes no array, sejam colocadas novamente
                if (sym.id == element.symptomId and
                        animalObj.id in illness.animals and
                        illness.id not in [ill.id for ill in illnessToPrint]):
                    illness.occurrences += element.symptomIntensity
                    illnessToPrint.append(illness)

    # Caso nenhuma doença seja encontrada, é informado o ocorrido
    if len(illnessToPrint) == 0:
        print("Não existe nenhuma doença que se encaixa nos sintomas informados")
    else:
        # Se alguma doença for encontrada é feito o calculo da porcentagem e o sort do array do maior pro menor
        for illnessForPrint in illnessToPrint:
            illnessForPrint.percentage = _calculateMedium(illnessForPrint)

        sortedIllness = sorted(illnessToPrint, key=lambda x: x.percentage, reverse=True)

        for validIllness in sortedIllness:
            print(f"- {validIllness.name} ({'%.2f' % validIllness.percentage}%)")
            print(f"  Sintomas: {_getIllnessSymptoms([ill.symptomId for ill in validIllness.symptoms])}")
            print(f"  Tratamento: {_getIllnessTreatments(validIllness.treatments)}")
            print(f"  Prevenção: {validIllness.prevention}")
            print("\n")

    input("\nPressione Enter para continuar...\n")


# Função que lista todas as vacinas de um animal
def _printVaccination():
    print(f"\nSegue abaixo as vacinas para {animalObj.name}")
    for vaccine in vaccineCycles:
        if vaccine.idAnimal == animalObj.id:
            print(f"{vaccine.name}")
            print(f"{vaccine.period}\n")

    input("\nPressione Enter para continuar...\n")


# Função que delega qual a opção selecionada para realizar uma ação (Mostrar vacinas, doenças, etc)
def _handleOption(opt: int):
    if opt == 1:
        _printPossibleIllness()
    elif opt == 2:
        _printVaccination()
    elif opt == 3:
        global animalObj
        animalObj = None
        global breedObj
        breedObj = None
        global animalWeight
        animalWeight = 0
    else:
        print("\nEncerrando programa...")
        global shouldProgramRun
        shouldProgramRun = False


# Função responsável por renderizar o menu principal, após o animal ser encontrado
def _printMainMenu():
    print(f"Animal: {animalObj.name}")
    print(f"Raça: {breedObj.name}\n")

    print(f"Peso: {animalWeight}kg | Peso ideal: {breedObj.idealWeight}kg")
    # Caso o peso do animal esteja acima do recomendado
    if animalWeight > breedObj.idealWeight:
        print(ANSI.BOLD + "Animal acima do peso!" + ANSI.END)
        print("Recomendações: Exercícios, e regularização da alimentação")

    # Caso o peso do animal esteja 3kg abaixo do recomendado
    if (breedObj.idealWeight - animalWeight) > 3:
        print(ANSI.BOLD + "Animal abaixo do peso!" + ANSI.END)
        print("Recomendações: Regularização da alimentação")

    print(f"\n{ANSI.UNDERLINE}Nutrição:{ANSI.END}")
    for nutrition in nutritions:
        if nutrition.id in breedObj.nutrition:
            print(
                f"{nutrition.description} - Consumo diário: {nutrition.quantity}{"g" if nutrition.quantityType == ENutritionQuantityType.GRAMS else "ml"}")

    print(f"\n{ANSI.UNDERLINE}Opções:{ANSI.END}")
    print("1- Consulta de sintomas")
    print("2- Ciclo vacinal")
    print("3- Informar outro animal")
    print("4- Encerrar o programa")

    # Chama a função para delegar a opção selecionada
    _handleOption(int(input("\nInforme a opção da lista acima: ")))


# Função que busca um objeto dentro da lista de acordo com o valor e propriedade informada
def _getObj(array: List[any], prop: str, value: any):
    for item in array:
        try:
            if getattr(item, prop).upper() == value.upper():
                return item
        except AttributeError:
            pass

    return None


# incialização do programa
while shouldProgramRun:
    # Enquanto não for encontrado um animal, é perguntado novamente
    while animalObj is None:
        animalName = input('Qual o animal que deseja consultar?\n')
        animalObj = _getObj(animals, "name", animalName)
        if animalObj is None:
            print("Animal não encontrado, tente novamente.\n")

    # Enquanto não for encontrado uma raça, é perguntado novamente
    while breedObj is None:
        breedName = input(f'Qual a raça do {animalObj.name}?\n')
        breedObj = _getObj(animalBreeds, "name", breedName)
        if breedObj is None:
            print("Raça não encontrada, tente novamente.\n")

    # Enquanto o peso informado não for maior que 0, é perguntado novamente
    while animalWeight <= 0:
        animalWeight = float(input('Qual o peso do seu animal? (em KG)\n'))
        if animalWeight <= 0:
            print("Peso precisa ser maior que 0.\n")

    # Chama a função para renderizar o menu principal
    if animalObj is not None and breedObj is not None and animalWeight != 0:
        _printMainMenu()
