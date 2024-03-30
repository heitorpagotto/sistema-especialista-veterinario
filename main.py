from data import animals, animalBreeds, nutritions, vaccineCycles, symptoms, illness, medications
from data import Animal, AnimalBreed, ENutritionQuantityType
from typing import List

# TODO: adicionar mais dados e ajustar os dados atuais

shouldProgramRun = True
animalObj: Animal = None
breedObj: AnimalBreed = None
animalWeight: float = 0.00


class ANSI:
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def _getIllnessSymptoms(symptomsId: List[int]):
    allSymptoms: List[str] = []
    for pos, symptomId in enumerate(symptomsId):
        for symptom in symptoms:
            if symptom.id == symptomId:
                allSymptoms.insert(pos, symptom.name)

    return ','.join(allSymptoms)


def _getIllnessTreatments(medicationIds: List[int]):
    allMedications: List[str] = []
    for pos, medicationId in enumerate(medicationIds):
        for medication in medications:
            if medication.id == medicationId:
                allMedications.insert(pos, medication.name)

    return ','.join(allMedications)


def _printPossibleIllness():
    symptomString = input("\nInforme os sintomas do animal separados por vírgula (não informe nada para retornar)\n")
    symptomSplit = symptomString.split(",")

    if len(symptomSplit) == 0:
        return

    symptomIds = []
    for pos, splitted in enumerate(symptomSplit):
        for symptom in symptoms:
            if symptom.name == splitted:
                symptomIds.insert(pos, symptom.id)
                break

    print("Seguem algumas potenciais doenças de acordo com os sintomas informados:\n")

    for illnesses in illness:
        if any(elem in illnesses.symptoms for elem in symptomIds):
            print(f"- {illnesses.name}")
            print(f"  Sintomas: {_getIllnessSymptoms(illnesses.symptoms)}")
            print(f"  Tratamento: {_getIllnessTreatments(illnesses.treatments)}")
            print(f"  Prevenção: {illnesses.prevention}")
            print("\n")

    input("\nPressione Enter para continuar...\n")


def _printVaccination():
    print(f"\nSegue abaixo as vacinas para {animalObj.name}")
    for vaccine in vaccineCycles:
        if vaccine.idAnimal == animalObj.id:
            print(f"{vaccine.name}")
            print(f"{vaccine.period}\n")

    input("\nPressione Enter para continuar...\n")


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


def _printMainMenu():
    print(f"Animal: {animalObj.name}")
    print(f"Raça: {breedObj.name}\n")

    print(f"Peso: {animalWeight}kg | Peso ideal: {breedObj.idealWeight}kg")
    if animalWeight > breedObj.idealWeight:
        print(ANSI.BOLD + "Animal acima do peso!" + ANSI.END)
        print("Recomendações: Exercícios, e regularização da alimentação")

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

    _handleOption(int(input("\nInforme a opção da lista acima: ")))


def _getObj(array: List[any], prop: str, value: any):
    for item in array:
        try:
            if getattr(item, prop) == value:
                return item
        except AttributeError:
            pass

    return None


while shouldProgramRun:
    while animalObj is None:
        animalName = input('Qual o animal que deseja consultar?\n')
        animalObj = _getObj(animals, "name", animalName)

    while breedObj is None:
        breedName = input(f'Qual a raça do {animalObj.name}?\n')
        breedObj = _getObj(animalBreeds, "name", breedName)

    while animalWeight <= 0:
        animalWeight = float(input('Qual o peso do seu animal? (em KG)\n'))

    if animalObj is not None and breedObj is not None and animalWeight != 0:
        _printMainMenu()
