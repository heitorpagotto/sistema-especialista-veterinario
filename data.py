from enum import Enum
from typing import List


class ENutritionQuantityType(Enum):
    GRAMS = 0
    MILLILITERS = 1


class EBreedBearing(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


class EMedicationType(Enum):
    INJECTION = 0
    PILL = 1


class DefaultClass:
    id: int
    description: str

    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description


class Animal:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class AnimalBreed:
    id: int
    name: str
    bearing: EBreedBearing
    idealWeight: float
    idAnimal: int
    nutrition: List[int]

    def __init__(self, id: int,
                 name: str,
                 bearing: EBreedBearing,
                 idealWeight: float,
                 idAnimal: int,
                 nutrition: List[int]):
        self.id = id
        self.name = name
        self.bearing = bearing
        self.idealWeight = idealWeight
        self.idAnimal = idAnimal
        self.nutrition = nutrition


class VaccineCycle:
    idAnimal: int
    name: str
    period: str

    def __init__(self, idAnimal: int, name: str, period: str):
        self.idAnimal = idAnimal
        self.name = name
        self.period = period


class Nutrition(DefaultClass):
    quantity: int
    quantityType: ENutritionQuantityType

    def __init__(self, id: int, description: str, quantity: int, quantityType: ENutritionQuantityType):
        super().__init__(id, description)
        self.quantity = quantity
        self.quantityType = quantityType


class Illness:
    id: int
    name: str
    symptoms: List[int]
    treatments: List[int]
    prevention: str

    def __init__(self, id: int, name: str, symptoms: List[int], treatments: List[int], prevention: str):
        self.id = id
        self.name = name
        self.symptoms = symptoms
        self.treatments = treatments
        self.prevention = prevention


class Symptoms:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Medication(DefaultClass):
    name: str
    type: EMedicationType

    def __init__(self, id: int, description: str, name: str, type: EMedicationType):
        super().__init__(id, description)
        self.name = name
        self.type = type


animals: List[Animal] = [
    Animal(1, "Cachorro"),
    Animal(2, "Pássaro"),
    Animal(3, "Gato")
]

nutritions: List[Nutrition] = [
    Nutrition(1, "Ração", 200, ENutritionQuantityType.GRAMS),
    Nutrition(2, "Tomar água", 2000, ENutritionQuantityType.MILLILITERS),
    Nutrition(3, "Aveia", 200, ENutritionQuantityType.GRAMS),
    Nutrition(4, "Sementes", 200, ENutritionQuantityType.GRAMS),
]

animalBreeds: List[AnimalBreed] = [
    AnimalBreed(1, "Husky Siberiano", EBreedBearing.LARGE, 25, 1, [1, 2]),
    AnimalBreed(2, "Pinscher", EBreedBearing.SMALL, 10, 1, [1, 2]),
    AnimalBreed(3, "Papagaio", EBreedBearing.MEDIUM, 0.5, 2, [1, 2]),
    AnimalBreed(4, "Calopsita", EBreedBearing.SMALL, 0.1, 2, [2, 3, 4]),
    AnimalBreed(5, "Persa", EBreedBearing.MEDIUM, 6, 3, [1, 2]),
    AnimalBreed(6, "Siamês", EBreedBearing.MEDIUM, 5.5, 3, [1, 2]),
]

vaccineCycles: List[VaccineCycle] = [
    VaccineCycle(1, "Vacina V10", "Aos 6 meses de idade"),
    VaccineCycle(1, "Vacina Antirrábica", "Quando filhote"),
    VaccineCycle(3, "Vacina Antirrábica", "Quando filhote"),
    VaccineCycle(1, "Vacina contra Leptospirose", "A cada 6 meses"),
    VaccineCycle(3, "Vacina FeLV", "Quando filhote"),
    VaccineCycle(3, "Vacina FVRCP", "Após as primeiras 6 semanas de vida"),
]

symptoms: List[Symptoms] = [
    Symptoms(1, "Coriza"),
    Symptoms(2, "Tosse"),
    Symptoms(3, "Perda de apetite"),
    Symptoms(4, "Febre"),
    Symptoms(5, "Vermelhidão"),
    Symptoms(6, "Inchaço"),
    Symptoms(7, "Vômito"),
    Symptoms(8, "Diarréia"),
    Symptoms(9, "Perda de peso"),
    Symptoms(10, "Fraqueza"),
    Symptoms(11, "Problema de plumagem"),
]

medications: List[Medication] = [
    Medication(1, "Tomar um comprimido a cada 12h", "Antibiótico", EMedicationType.PILL),
    Medication(2, "Tomar um comprimido por dia", "Anti-Alérgico", EMedicationType.PILL),
    Medication(3, "Tomar um comprimido por dia", "Analgésico", EMedicationType.PILL),
    Medication(4, "Tomar um comprimido por dia", "Anti-fungicos", EMedicationType.PILL),
    Medication(5, "Alivia desidratração", "Fluído terapia", EMedicationType.INJECTION),
    Medication(6, "Vitaminas complementares", "Vitaminas", EMedicationType.PILL),
    Medication(7, "Tomar um comprimido por dia", "Anti-inflamatório", EMedicationType.PILL),
    Medication(8, "Tomar um comprimido por dia", "Anti-parasitário", EMedicationType.PILL),
]

illness: List[Illness] = [
    Illness(1, "Traqueobronquite", [1, 2, 4, 3], [1, 7, 3, 5, 6], "Vacinação em dia e higiene constante ajudam na prevenção da doença"),
    Illness(2, "Piodermite", [5, 6], [1, 2], "Higiene e secagem apropriada após banhos"),
    Illness(3, "Doença do carrapato", [3, 4], [1], "Vacinação em dia e controle de ambientes silvestres ao qual o animal tem contato"),
    Illness(4, "Leptospirose", [4, 7, 8], [1, 5, 3], "Vacinação em dia, controle de roedores no local e higiene constante"),
    Illness(5, "Toxoplasmose", [4, 7, 8], [8], "Alimentação e água seguras e limpas e higiene constante"),
    Illness(6, "Candidíase", [4, 7, 8], [4], "Controle de parasitas, higiene constante e manter uma alimentação balanceada"),
    Illness(7, "Deficiencia Nutricional", [10, 11, 9], [6, 5], "Alimentação balanceada de acordo com o animal"),
]
