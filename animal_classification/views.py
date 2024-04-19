from aima.logic import *
from aima.utils import *
import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

questions_list = [
    {
        "id": 1,
        "question": "Does your animal have a BACKBONE?",
        "YES": 2,
        "NO": 32,
    },
    {
        "id": 2,
        "question": "Is the animal warm blooded?",
        "YES": 3,
        "NO": 26,
    },
    {
        "id": 3,
        "question": "Normally, does the female of your animal nurse its young with milk?",
        "YES": 4,
        "NO": "end",
    },
    {
        "id": 4,
        "question": "Does your animal eat red meat?",
        "YES": 5,
        "NO": 13,
    },
    {
        "id": 5,
        "question": "Can your animal fly?",
        "YES": "end",
        "NO": 6,
    },
    {
        "id": 6,
        "question": "Does your animal have an opposing thumb?",
        "YES": 7,
        "NO": 10,
    },
    {
        "id": 7,
        "question": "Does your animal have a prehensile tail?",
        "YES": "end",
        "NO": 8,
    },
    {
        "id": 8,
        "question": "Is your animal nearly hairless?",
        "YES": "end",
        "NO": 9,
    },
    {
        "id": 9,
        "question": "Does your animal have long, powerful arms?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 10,
        "question": "Does an adult normally weigh over 400 pounds?",
        "YES": 11,
        "NO": 12,
    },
    {
        "id": 11,
        "question": "Is your animal land based?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 12,
        "question": "Does your animal have a thin tail?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 13,
        "question": "Does your animal have hooves?",
        "YES": 14,
        "NO": 21,
    },
    {
        "id": 14,
        "question": "Does your animal stand on two toes__hooves per foot?",
        "YES": 15,
        "NO": 20,
    },
    {
        "id": 15,
        "question": "Does your animal have horns?",
        "YES": 16,
        "NO": 18,
    },
    {
        "id": 16,
        "question": "Does your animal have fleece?",
        "YES": "end",
        "NO": 17,
    },
    {
        "id": 17,
        "question": "Is your animal domesticated?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 18,
        "question": "Does your animal normally live in the desert?",
        "YES": "end",
        "NO": 19,
    },
    {
        "id": 19,
        "question": "Is your animal semi-aquatic?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 20,
        "question": "Is your animal covered with a protective plating?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 21,
        "question": "Does your animal live in water?",
        "YES": 22,
        "NO": 23,
    },
    {
        "id": 22,
        "question": "Is your animal, unfortunately, commercially hunted?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 23,
        "question": "Does your animal have large front teeth?",
        "YES": 24,
        "NO": 25,
    },
    {
        "id": 24,
        "question": "Does your animal have large ears?",
        "YES": "end",
        "NO": "end"
    },
    {
        "id": 25,
        "question": "Does your animal have a pouch?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 26,
        "question": "Is your animal always in water?",
        "YES": 27,
        "NO": 28,
    },
    {
        "id": 27,
        "question": "Does your animal have a boney skeleton?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 28,
        "question": "Is your animal covered with scaled skin?",
        "YES": 29,
        "NO": 31,
    },
    {
        "id": 29,
        "question": "Does the animal have a rounded shell?",
        "YES": "end",
        "NO": 30,
    },
    {
        "id": 30,
        "question": "Does your animal have limbs?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 31,
        "question": "Does your animal jump?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 32,
        "question": "Does your animal live primarily in soil?",
        "YES": 33,
        "NO": 34,
    },
    {
        "id": 33,
        "question": "Does your animal have a flat body?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 34,
        "question": "Is the animal's body in segments?",
        "YES": 35,
        "NO": 37,
    },
    {
        "id": 35,
        "question": "Does your animal have a shell?",
        "YES": 36,
        "NO": "end",
    },
    {
        "id": 36,
        "question": "Does your animal have a tail?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 37,
        "question": "Does your animal use many cells to digest its food instead of a stomach?",
        "YES": 38,
        "NO": 40,
    },
    {
        "id": 38,
        "question": "Is your animal attached permanently to an object?",
        "YES": 39,
        "NO": "end",
    },
    {
        "id": 39,
        "question": "Does your animal normally have spikes radiating from its body?",
        "YES": "end",
        "NO": "end",
    },
    {
        "id": 40,
        "question": "Is your animal made up of more than one cell?",
        "YES": 41,
        "NO": "end",
    },
    {
        "id": 41,
        "question": "Does your animal have a spiral__shaped shell?",
        "YES": "end",
        "NO": 42,
    },
    {
        "id": 42,
        "question": "Is your animal protected by two half__shells?",
        "YES": "end",
        "NO": "end",
    },
]
rules = [
    'BACKBONE',
    'WARM_BLOODED',
    'HAS_BREASTS',
    'CAN_EAT_MEAT',
    'FLY',
    'OPPOSING_THUMB',
    'PREHENSILE_TAIL',
    'NEARLY_HAIRLESS',
    'LONG_POWERFUL_ARMS',
    'OVER_400',
    'LAND_BASED',
    'THINTAIL',
    'HOOVES',
    'TWO_TOES',
    'HORNS',
    'FLEECE',
    'DOMESTICATED',
    'LIVES_IN_DESERT',
    'SEMI_AQUATIC',
    'PLATING',
    'LIVE_IN_WATER',
    'HUNTED',
    'FRONT_TEETH',
    'LARGE_EARS',
    'POUCH',
    'ALWAYS_IN_WATER',
    'BONEY',
    'SCALY',
    'ROUNDED_SHELL',
    'LIMBS',
    'JUMP',
    'LIVE_PRIME_IN_SOIL',
    'FLAT_BODIED',
    'BODY_IN_SEGMENTS',
    'SHELL',
    'TAIL',
    'DIGEST_CELLS',
    'STATIONARY',
    'SPIKES',
    'MULTICELLED',
    'SPIRAL_SHELL',
    'BIVALVE',
]
answers = []

next_question_id = 1
last_question_id = 0
last_answer = ''

kb = FolKB()


def animal_kb():
    kb.tell(expr('ANSWER(YES)'))
    kb.tell(expr('ANSWER(NO)'))
    kb.tell(expr('TYPE_ANIMAL(FLATWORM)'))
    kb.tell(expr('TYPE_ANIMAL(BIRD__PENGUIN)'))
    kb.tell(expr('TYPE_ANIMAL(WORM__LEECH)'))
    kb.tell(expr('TYPE_ANIMAL(FISH)'))
    kb.tell(expr('TYPE_ANIMAL(SHARK__RAY)'))
    kb.tell(expr('TYPE_ANIMAL(CENTIPEDE__MILLIPEDE__INSECT)'))
    kb.tell(expr('TYPE_ANIMAL(BAT)'))
    kb.tell(expr('TYPE_ANIMAL(TURTLE)'))
    kb.tell(expr('TYPE_ANIMAL(FROG)'))
    kb.tell(expr('TYPE_ANIMAL(SALAMANDER)'))
    kb.tell(expr('TYPE_ANIMAL(LOBSTER)'))
    kb.tell(expr('TYPE_ANIMAL(CRAB)'))
    kb.tell(expr('TYPE_ANIMAL(JELLYFISH)'))
    kb.tell(expr('TYPE_ANIMAL(PROTOZOA)'))
    kb.tell(expr('TYPE_ANIMAL(CROCODILE__ALLIGATOR)'))
    kb.tell(expr('TYPE_ANIMAL(SNAKE)'))
    kb.tell(expr('TYPE_ANIMAL(SEA_ANEMONE)'))
    kb.tell(expr('TYPE_ANIMAL(CORAL__SPONGE)'))
    kb.tell(expr('TYPE_ANIMAL(SNAIL)'))
    kb.tell(expr('TYPE_ANIMAL(MONKEY)'))
    kb.tell(expr('TYPE_ANIMAL(RHINOCEROS)'))
    kb.tell(expr('TYPE_ANIMAL(HORSE__ZEBRA)'))
    kb.tell(expr('TYPE_ANIMAL(WHALE)'))
    kb.tell(expr('TYPE_ANIMAL(DOLPHIN__PORPOISE)'))
    kb.tell(expr('TYPE_ANIMAL(CLAM__OYSTER)'))
    kb.tell(expr('TYPE_ANIMAL(SQUID__OCTOPUS)'))
    kb.tell(expr('TYPE_ANIMAL(MAN)'))
    kb.tell(expr('TYPE_ANIMAL(BEAR__TIGER__LION)'))
    kb.tell(expr('TYPE_ANIMAL(WALRUS)'))
    kb.tell(expr('TYPE_ANIMAL(CAT)'))
    kb.tell(expr('TYPE_ANIMAL(COYOTE__WOLF__FOX__DOG)'))
    kb.tell(expr('TYPE_ANIMAL(CAMEL)'))
    kb.tell(expr('TYPE_ANIMAL(GIRAFFE)'))
    kb.tell(expr('TYPE_ANIMAL(HIPPOPOTAMUS)'))
    kb.tell(expr('TYPE_ANIMAL(RABBIT)'))
    kb.tell(expr('TYPE_ANIMAL(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE)'))
    kb.tell(expr('TYPE_ANIMAL(KANGAROO__KOALA_BEAR)'))
    kb.tell(expr('TYPE_ANIMAL(MOLE__SHREW__ELEPHANT)'))
    kb.tell(expr('TYPE_ANIMAL(SHEEP__GOAT)'))
    kb.tell(expr('TYPE_ANIMAL(ORANGUTAN__GORILLA__CHIMPANZEE)'))
    kb.tell(expr('TYPE_ANIMAL(BABOON)'))
    kb.tell(expr('TYPE_ANIMAL(COW)'))
    kb.tell(expr('TYPE_ANIMAL(DEER__MOOSE__ANTELOPE)'))

    kb.tell(expr('BACKBONE(BAT, YES)'))
    kb.tell(expr('BACKBONE(MONKEY, YES)'))
    kb.tell(expr('BACKBONE(MAN, YES)'))
    kb.tell(expr('BACKBONE(BEAR__TIGER__LION, YES)'))
    kb.tell(expr('BACKBONE(WALRUS, YES)'))
    kb.tell(expr('BACKBONE(CAT, YES)'))
    kb.tell(expr('BACKBONE(COYOTE__WOLF__FOX__DOG, YES)'))
    kb.tell(expr('BACKBONE(ORANGUTAN__GORILLA__CHIMPANZEE, YES)'))
    kb.tell(expr('BACKBONE(BABOON, YES)'))
    kb.tell(expr('BACKBONE(RHINOCEROS, YES)'))
    kb.tell(expr('BACKBONE(HORSE__ZEBRA, YES)'))
    kb.tell(expr('BACKBONE(WHALE, YES)'))
    kb.tell(expr('BACKBONE(DOLPHIN__PORPOISE, YES)'))
    kb.tell(expr('BACKBONE(CAMEL, YES)'))
    kb.tell(expr('BACKBONE(GIRAFFE, YES)'))
    kb.tell(expr('BACKBONE(HIPPOPOTAMUS, YES)'))
    kb.tell(expr('BACKBONE(RABBIT, YES)'))
    kb.tell(expr('BACKBONE(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, YES)'))
    kb.tell(expr('BACKBONE(KANGAROO__KOALA_BEAR, YES)'))
    kb.tell(expr('BACKBONE(MOLE__SHREW__ELEPHANT, YES)'))
    kb.tell(expr('BACKBONE(SHEEP__GOAT, YES)'))
    kb.tell(expr('BACKBONE(COW, YES)'))
    kb.tell(expr('BACKBONE(DEER__MOOSE__ANTELOPE, YES)'))
    kb.tell(expr('BACKBONE(BIRD__PENGUIN, YES)'))
    kb.tell(expr('BACKBONE(FISH, YES)'))
    kb.tell(expr('BACKBONE(SHARK__RAY, YES)'))
    kb.tell(expr('BACKBONE(TURTLE, YES)'))
    kb.tell(expr('BACKBONE(FROG, YES)'))
    kb.tell(expr('BACKBONE(SALAMANDER, YES)'))
    kb.tell(expr('BACKBONE(CROCODILE__ALLIGATOR, YES)'))
    kb.tell(expr('BACKBONE(SNAKE, YES)'))
    kb.tell(expr('BACKBONE(FLATWORM, NO)'))
    kb.tell(expr('BACKBONE(WORM__LEECH, NO)'))
    kb.tell(expr('BACKBONE(CENTIPEDE__MILLIPEDE__INSECT, NO)'))
    kb.tell(expr('BACKBONE(LOBSTER, NO)'))
    kb.tell(expr('BACKBONE(CRAB, NO)'))
    kb.tell(expr('BACKBONE(JELLYFISH, NO)'))
    kb.tell(expr('BACKBONE(PROTOZOA, NO)'))
    kb.tell(expr('BACKBONE(SEA_ANEMONE, NO)'))
    kb.tell(expr('BACKBONE(CORAL__SPONGE, NO)'))
    kb.tell(expr('BACKBONE(SNAIL, NO)'))
    kb.tell(expr('BACKBONE(SQUID__OCTOPUS, NO)'))
    kb.tell(expr('BACKBONE(CLAM__OYSTER, NO)'))
    kb.tell(expr('WARM_BLOODED(YES)'))
    kb.tell(expr('WARM_BLOODED(BAT, YES)'))
    kb.tell(expr('WARM_BLOODED(MONKEY, YES)'))
    kb.tell(expr('WARM_BLOODED(MAN, YES)'))
    kb.tell(expr('WARM_BLOODED(BEAR__TIGER__LION, YES)'))
    kb.tell(expr('WARM_BLOODED(WALRUS, YES)'))
    kb.tell(expr('WARM_BLOODED(CAT, YES)'))
    kb.tell(expr('WARM_BLOODED(COYOTE__WOLF__FOX__DOG, YES)'))
    kb.tell(expr('WARM_BLOODED(ORANGUTAN__GORILLA__CHIMPANZEE, YES)'))
    kb.tell(expr('WARM_BLOODED(BABOON, YES)'))
    kb.tell(expr('WARM_BLOODED(RHINOCEROS, YES)'))
    kb.tell(expr('WARM_BLOODED(HORSE__ZEBRA, YES)'))
    kb.tell(expr('WARM_BLOODED(WHALE, YES)'))
    kb.tell(expr('WARM_BLOODED(DOLPHIN__PORPOISE, YES)'))
    kb.tell(expr('WARM_BLOODED(CAMEL, YES)'))
    kb.tell(expr('WARM_BLOODED(GIRAFFE, YES)'))
    kb.tell(expr('WARM_BLOODED(HIPPOPOTAMUS, YES)'))
    kb.tell(expr('WARM_BLOODED(RABBIT, YES)'))
    kb.tell(expr('WARM_BLOODED(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, YES)'))
    kb.tell(expr('WARM_BLOODED(KANGAROO__KOALA_BEAR, YES)'))
    kb.tell(expr('WARM_BLOODED(MOLE__SHREW__ELEPHANT, YES)'))
    kb.tell(expr('WARM_BLOODED(SHEEP__GOAT, YES)'))
    kb.tell(expr('WARM_BLOODED(COW, YES)'))
    kb.tell(expr('WARM_BLOODED(DEER__MOOSE__ANTELOPE, YES)'))
    kb.tell(expr('WARM_BLOODED(BIRD__PENGUIN, YES)'))
    kb.tell(expr('WARM_BLOODED(FISH, NO)'))
    kb.tell(expr('WARM_BLOODED(SHARK__RAY, NO)'))
    kb.tell(expr('WARM_BLOODED(TURTLE, NO)'))
    kb.tell(expr('WARM_BLOODED(FROG, NO)'))
    kb.tell(expr('WARM_BLOODED(SALAMANDER, NO)'))
    kb.tell(expr('WARM_BLOODED(CROCODILE__ALLIGATOR, NO)'))
    kb.tell(expr('WARM_BLOODED(SNAKE, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(FLATWORM, YES)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(WORM__LEECH, YES)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(CENTIPEDE__MILLIPEDE__INSECT, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(LOBSTER, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(CRAB, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(JELLYFISH, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(PROTOZOA, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(SEA_ANEMONE, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(CORAL__SPONGE, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(SNAIL, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(SQUID__OCTOPUS, NO)'))
    kb.tell(expr('LIVE_PRIME_IN_SOIL(CLAM__OYSTER, NO)'))
    kb.tell(expr('HAS_BREASTS(BAT, YES)'))
    kb.tell(expr('HAS_BREASTS(MONKEY, YES)'))
    kb.tell(expr('HAS_BREASTS(MAN, YES)'))
    kb.tell(expr('HAS_BREASTS(BEAR__TIGER__LION, YES)'))
    kb.tell(expr('HAS_BREASTS(WALRUS, YES)'))
    kb.tell(expr('HAS_BREASTS(CAT, YES)'))
    kb.tell(expr('HAS_BREASTS(COYOTE__WOLF__FOX__DOG, YES)'))
    kb.tell(expr('HAS_BREASTS(ORANGUTAN__GORILLA__CHIMPANZEE, YES)'))
    kb.tell(expr('HAS_BREASTS(BABOON, YES)'))
    kb.tell(expr('HAS_BREASTS(RHINOCEROS, YES)'))
    kb.tell(expr('HAS_BREASTS(HORSE__ZEBRA, YES)'))
    kb.tell(expr('HAS_BREASTS(WHALE, YES)'))
    kb.tell(expr('HAS_BREASTS(DOLPHIN__PORPOISE, YES)'))
    kb.tell(expr('HAS_BREASTS(CAMEL, YES)'))
    kb.tell(expr('HAS_BREASTS(GIRAFFE, YES)'))
    kb.tell(expr('HAS_BREASTS(HIPPOPOTAMUS, YES)'))
    kb.tell(expr('HAS_BREASTS(RABBIT, YES)'))
    kb.tell(expr('HAS_BREASTS(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, YES)'))
    kb.tell(expr('HAS_BREASTS(KANGAROO__KOALA_BEAR, YES)'))
    kb.tell(expr('HAS_BREASTS(MOLE__SHREW__ELEPHANT, YES)'))
    kb.tell(expr('HAS_BREASTS(SHEEP__GOAT, YES)'))
    kb.tell(expr('HAS_BREASTS(COW, YES)'))
    kb.tell(expr('HAS_BREASTS(DEER__MOOSE__ANTELOPE, YES)'))
    kb.tell(expr('HAS_BREASTS(BIRD__PENGUIN, NO)'))
    kb.tell(expr('ALWAYS_IN_WATER(FISH, YES)'))
    kb.tell(expr('ALWAYS_IN_WATER(SHARK__RAY, YES)'))
    kb.tell(expr('ALWAYS_IN_WATER(TURTLE, NO)'))
    kb.tell(expr('ALWAYS_IN_WATER(FROG, NO)'))
    kb.tell(expr('ALWAYS_IN_WATER(SALAMANDER, NO)'))
    kb.tell(expr('ALWAYS_IN_WATER(CROCODILE__ALLIGATOR, NO)'))
    kb.tell(expr('ALWAYS_IN_WATER(SNAKE, NO)'))
    kb.tell(expr('FLAT_BODIED(FLATWORM, YES)'))
    kb.tell(expr('FLAT_BODIED(WORM__LEECH, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(CENTIPEDE__MILLIPEDE__INSECT, YES)'))
    kb.tell(expr('BODY_IN_SEGMENTS(LOBSTER, YES)'))
    kb.tell(expr('BODY_IN_SEGMENTS(CRAB, YES)'))
    kb.tell(expr('BODY_IN_SEGMENTS(JELLYFISH, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(PROTOZOA, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(SEA_ANEMONE, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(CORAL__SPONGE, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(SNAIL, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(SQUID__OCTOPUS, NO)'))
    kb.tell(expr('BODY_IN_SEGMENTS(CLAM__OYSTER, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(BAT, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(MONKEY, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(MAN, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(BEAR__TIGER__LION, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(WALRUS, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(CAT, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(COYOTE__WOLF__FOX__DOG, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(ORANGUTAN__GORILLA__CHIMPANZEE, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(BABOON, YES)'))
    kb.tell(expr('CAN_EAT_MEAT(RHINOCEROS, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(HORSE__ZEBRA, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(WHALE, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(DOLPHIN__PORPOISE, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(CAMEL, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(GIRAFFE, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(HIPPOPOTAMUS, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(RABBIT, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(KANGAROO__KOALA_BEAR, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(MOLE__SHREW__ELEPHANT, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(SHEEP__GOAT, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(COW, NO)'))
    kb.tell(expr('CAN_EAT_MEAT(DEER__MOOSE__ANTELOPE, NO)'))
    kb.tell(expr('BONEY(FISH, YES)'))
    kb.tell(expr('BONEY(SHARK__RAY, NO)'))
    kb.tell(expr('SCALY(TURTLE, YES)'))
    kb.tell(expr('SCALY(CROCODILE__ALLIGATOR, YES)'))
    kb.tell(expr('SCALY(SNAKE, YES)'))
    kb.tell(expr('SCALY(FROG, NO)'))
    kb.tell(expr('SCALY(SALAMANDER, NO)'))
    kb.tell(expr('SHELL(LOBSTER, YES)'))
    kb.tell(expr('SHELL(CRAB, YES)'))
    kb.tell(expr('SHELL(CENTIPEDE__MILLIPEDE__INSECT, NO)'))
    kb.tell(expr('DIGEST_CELLS(JELLYFISH, YES)'))
    kb.tell(expr('DIGEST_CELLS(SEA_ANEMONE, YES)'))
    kb.tell(expr('DIGEST_CELLS(CORAL__SPONGE, YES)'))
    kb.tell(expr('DIGEST_CELLS(PROTOZOA, NO)'))
    kb.tell(expr('DIGEST_CELLS(SNAIL, NO)'))
    kb.tell(expr('DIGEST_CELLS(SQUID__OCTOPUS, NO)'))
    kb.tell(expr('DIGEST_CELLS(CLAM__OYSTER, NO)'))
    kb.tell(expr('FLY(BAT, YES)'))
    kb.tell(expr('FLY(MAN, NO)'))
    kb.tell(expr('FLY(BEAR__TIGER__LION, NO)'))
    kb.tell(expr('FLY(WALRUS, NO)'))
    kb.tell(expr('FLY(CAT, NO)'))
    kb.tell(expr('FLY(COYOTE__WOLF__FOX__DOG, NO)'))
    kb.tell(expr('FLY(ORANGUTAN__GORILLA__CHIMPANZEE, NO)'))
    kb.tell(expr('FLY(BABOON, NO)'))
    kb.tell(expr('HOOVES(RHINOCEROS, YES)'))
    kb.tell(expr('HOOVES(HORSE__ZEBRA, YES)'))
    kb.tell(expr('HOOVES(CAMEL, YES)'))
    kb.tell(expr('HOOVES(GIRAFFE, YES)'))
    kb.tell(expr('HOOVES(HIPPOPOTAMUS, YES)'))
    kb.tell(expr('HOOVES(SHEEP__GOAT, YES)'))
    kb.tell(expr('HOOVES(COW, YES)'))
    kb.tell(expr('HOOVES(DEER__MOOSE__ANTELOPE, YES)'))
    kb.tell(expr('HOOVES(WHALE, NO)'))
    kb.tell(expr('HOOVES(DOLPHIN__PORPOISE, NO)'))
    kb.tell(expr('HOOVES(RABBIT, NO)'))
    kb.tell(expr('HOOVES(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, NO)'))
    kb.tell(expr('HOOVES(KANGAROO__KOALA_BEAR, NO)'))
    kb.tell(expr('HOOVES(MOLE__SHREW__ELEPHANT, NO)'))
    kb.tell(expr('ROUNDED_SHELL(TURTLE, YES)'))
    kb.tell(expr('ROUNDED_SHELL(CROCODILE__ALLIGATOR, NO)'))
    kb.tell(expr('ROUNDED_SHELL(SNAKE, NO)'))
    kb.tell(expr('JUMP(CRAB, YES)'))
    kb.tell(expr('JUMP(SALAMANDER, NO)'))
    kb.tell(expr('TAIL(LOBSTER, YES)'))
    kb.tell(expr('TAIL(CRAB, NO)'))
    kb.tell(expr('STATIONARY(SEA_ANEMONE, YES)'))
    kb.tell(expr('STATIONARY(CORAL__SPONGE, YES)'))
    kb.tell(expr('STATIONARY(JELLYFISH, NO)'))
    kb.tell(expr('MULTICELLED(SNAIL, YES)'))
    kb.tell(expr('MULTICELLED(CLAM__OYSTER, YES)'))
    kb.tell(expr('MULTICELLED(SQUID__OCTOPUS, YES)'))
    kb.tell(expr('MULTICELLED(PROTOZOA, NO)'))
    kb.tell(expr('OPPOSING_THUMB(MONKEY, YES)'))
    kb.tell(expr('OPPOSING_THUMB(MAN, YES)'))
    kb.tell(expr('OPPOSING_THUMB(ORANGUTAN__GORILLA__CHIMPANZEE, YES)'))
    kb.tell(expr('OPPOSING_THUMB(BABOON, YES)'))
    kb.tell(expr('OPPOSING_THUMB(BEAR__TIGER__LION, NO)'))
    kb.tell(expr('OPPOSING_THUMB(WALRUS, NO)'))
    kb.tell(expr('OPPOSING_THUMB(CAT, NO)'))
    kb.tell(expr('OPPOSING_THUMB(COYOTE__WOLF__FOX__DOG, NO)'))
    kb.tell(expr('TWO_TOES(CAMEL, YES)'))
    kb.tell(expr('TWO_TOES(GIRAFFE, YES)'))
    kb.tell(expr('TWO_TOES(HIPPOPOTAMUS, YES)'))
    kb.tell(expr('TWO_TOES(SHEEP__GOAT, YES)'))
    kb.tell(expr('TWO_TOES(COW, YES)'))
    kb.tell(expr('TWO_TOES(DEER__MOOSE__ANTELOPE, YES)'))
    kb.tell(expr('TWO_TOES(RHINOCEROS, NO)'))
    kb.tell(expr('TWO_TOES(HORSE__ZEBRA, NO)'))
    kb.tell(expr('LIVE_IN_WATER(WHALE, YES)'))
    kb.tell(expr('LIVE_IN_WATER(DOLPHIN__PORPOISE, YES)'))
    kb.tell(expr('LIVE_IN_WATER(RABBIT, NO)'))
    kb.tell(expr('LIVE_IN_WATER(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, NO)'))
    kb.tell(expr('LIVE_IN_WATER(KANGAROO__KOALA_BEAR, NO)'))
    kb.tell(expr('LIVE_IN_WATER(MOLE__SHREW__ELEPHANT, NO)'))
    kb.tell(expr('LIMBS(CROCODILE__ALLIGATOR, YES)'))
    kb.tell(expr('LIMBS(SNAKE, NO)'))
    kb.tell(expr('SPIKEs(SEA_ANEMONE, YES)'))
    kb.tell(expr('SPIKEs(CORAL__SPONGE, NO)'))
    kb.tell(expr('SPIRAL_SHELL(SNAIL, YES)'))
    kb.tell(expr('SPIRAL_SHELL(CLAM__OYSTER, NO)'))
    kb.tell(expr('SPIRAL_SHELL(SQUID__OCTOPUS, NO)'))
    kb.tell(expr('PREHENSILE_TAIL(MONKEY, YES)'))
    kb.tell(expr('PREHENSILE_TAIL(MAN, NO)'))
    kb.tell(expr('PREHENSILE_TAIL(ORANGUTAN__GORILLA__CHIMPANZEE, NO)'))
    kb.tell(expr('PREHENSILE_TAIL(BABOON, NO)'))
    kb.tell(expr('OVER_400(BEAR__TIGER__LION, YES)'))
    kb.tell(expr('OVER_400(WALRUS, YES)'))
    kb.tell(expr('OVER_400(CAT, NO)'))
    kb.tell(expr('OVER_400(COYOTE__WOLF__FOX__DOG, NO)'))
    kb.tell(expr('horns(SHEEP__GOAT, YES)'))
    kb.tell(expr('HORNS(COW, YES)'))
    kb.tell(expr('HORNS(DEER__MOOSE__ANTELOPE, YES)'))
    kb.tell(expr('HORNS(CAMEL, NO)'))
    kb.tell(expr('HORNS(GIRAFFE, NO)'))
    kb.tell(expr('HORNS(HIPPOPOTAMUS, NO)'))
    kb.tell(expr('PLATING(RHINOCEROS, YES)'))
    kb.tell(expr('PLATING(HORSE__ZEBRA, NO)'))
    kb.tell(expr('HUNTED(WHALE, YES)'))
    kb.tell(expr('HUNTED(DOLPHIN__PORPOISE,NO)'))
    kb.tell(expr('FRONT_TEETH(RABBIT, YES)'))
    kb.tell(expr('FRONT_TEETH(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, YES)'))
    kb.tell(expr('FRONT_TEETH(KANGAROO__KOALA_BEAR, NO)'))
    kb.tell(expr('FRONT_TEETH(MOLE__SHREW__ELEPHANT, NO)'))
    kb.tell(expr('BIVALVE(CLAM__OYSTER, YES)'))
    kb.tell(expr('BIVALVE(SQUID__OCTOPUS, NO)'))
    kb.tell(expr('NEARLY_HAIRLESS(MAN, YES)'))
    kb.tell(expr('NEARLY_HAIRLESS(ORANGUTAN__GORILLA__CHIMPANZEE, NO)'))
    kb.tell(expr('NEARLY_HAIRLESS(BABOON, NO)'))
    kb.tell(expr('LAND_BASED(BEAR__TIGER__LION, YES)'))
    kb.tell(expr('LAND_BASED(WALRUS, NO)'))
    kb.tell(expr('THINTAIL(CAT, YES)'))
    kb.tell(expr('THINTAIL(COYOTE__WOLF__FOX__DOG, NO)'))
    kb.tell(expr('LIVES_IN_DESERT(CAMEL, YES)'))
    kb.tell(expr('LIVES_IN_DESERT(GIRAFFE, NO)'))
    kb.tell(expr('LIVES_IN_DESERT(HIPPOPOTAMUS, NO)'))
    kb.tell(expr('SEMI_AQUATIC(GIRAFFE, NO)'))
    kb.tell(expr('SEMI_AQUATIC(HIPPOPOTAMUS, YES)'))
    kb.tell(expr('LARGE_EARS(RABBIT, YES)'))
    kb.tell(expr('LARGE_EARS(RAT__MOUSE__SQUIRREL__BEAVER__PORCUPINE, NO)'))
    kb.tell(expr('POUCH(KANGAROO__KOALA_BEAR, YES)'))
    kb.tell(expr('POUCH(MOLE__SHREW__ELEPHANT, NO)'))
    kb.tell(expr('FLEECE(SHEEP__GOAT, YES)'))
    kb.tell(expr('FLEECE(DEER__MOOSE__ANTELOPE, NO)'))
    kb.tell(expr('LONG_POWERFUL_ARMS(ORANGUTAN__GORILLA__CHIMPANZEE, YES)'))
    kb.tell(expr('LONG_POWERFUL_ARMS(BABOON, NO)'))
    kb.tell(expr('DOMESTICATED(COW, YES)'))
    kb.tell(expr('DOMESTICATED(DEER__MOOSE__ANTELOPE, NO)'))

    # Rules
    kb.tell(expr('BACKBONE(x, YES) ==> SUPERPHYLUM(x,BACKBONE)'))
    kb.tell(expr('BACKBONE(x, NO) ==> SUPERPHYLUM(x,JELLYBACK)'))

    kb.tell(expr('SUPERPHYLUM(x,BACKBONE) & WARM_BLOODED(x, YES) ==> PHYLUM(x,WARM)'))
    kb.tell(expr('SUPERPHYLUM(x,BACKBONE) & WARM_BLOODED(x, NO) ==> PHYLUM(x,COLD)'))
    kb.tell(expr('SUPERPHYLUM(x,JELLYBACK) & LIVE_PRIME_IN_SOIL(x, YES) ==> PHYLUM(x,SOIL)'))
    kb.tell(expr('SUPERPHYLUM(x,JELLYBACK) & LIVE_PRIME_IN_SOIL(x, NO) ==> PHYLUM(x,ELSEWHERE)'))

    kb.tell(expr('PHYLUM(x,WARM) & HAS_BREASTS(x, YES) ==> CLASS_IN(x,BREASTS)'))
    kb.tell(expr('PHYLUM(x,WARM) & HAS_BREASTS(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('PHYLUM(x,COLD) & ALWAYS_IN_WATER(x, YES) ==> CLASS_IN(x,WATER)'))
    kb.tell(expr('PHYLUM(x,COLD) & ALWAYS_IN_WATER(x, NO) ==> CLASS_IN(x,DRY)'))
    kb.tell(expr('PHYLUM(x,SOIL) & FLAT_BODIED(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('PHYLUM(x,SOIL) & FLAT_BODIED(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('PHYLUM(x,ELSEWHERE) & BODY_IN_SEGMENTS(x, YES) ==> CLASS_IN(x,SEGMENTS)'))
    kb.tell(expr('PHYLUM(x,ELSEWHERE) & BODY_IN_SEGMENTS(x, NO) ==> CLASS_IN(x,UNIFIED)'))

    kb.tell(expr('CLASS_IN(x,BREASTS) & CAN_EAT_MEAT(x, YES) ==> ORDER(x,MEAT)'))
    kb.tell(expr('CLASS_IN(x,BREASTS) & CAN_EAT_MEAT(x, NO) ==> ORDER(x,VEGY)'))
    kb.tell(expr('CLASS_IN(x,WATER) & BONEY(x, YES) ==> type_animal(x)'))
    kb.tell(expr('class_in(x,WATER) & BONEY(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('CLASS_IN(x,DRY) & SCALY(x, YES) ==> ORDER(x,SCALES)'))
    kb.tell(expr('CLASS_IN(x,DRY) & SCALY(x, NO) ==> ORDER(x,SOFT)'))
    kb.tell(expr('CLASS_IN(x,SEGMENTS) & SHELL(x, YES) ==> ORDER(x,SHELL)'))
    kb.tell(expr('CLASS_IN(x,SEGMENTS) & SHELL(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('CLASS_IN(x,UNIFIED) & DIGEST_CELLS(x, YES) ==> ORDER(x,CELLS)'))
    kb.tell(expr('CLASS_IN(x,UNIFIED) & DIGEST_CELLS(x, NO) ==> ORDER(x,STOMACH)'))

    kb.tell(expr('ORDER(x,MEAT) & FLY(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,MEAT) & FLY(x, NO) ==> FAMILY(x,NOWINGS)'))
    kb.tell(expr('ORDER(x,VEGY) & HOOVES(x, YES) ==> FAMILY(x,HOOVES)'))
    kb.tell(expr('ORDER(x,VEGY) & HOOVES(x, NO) ==> FAMILY(x,FEET)'))
    kb.tell(expr('ORDER(x,SCALES) & ROUNDED_SHELL(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,SCALES) & ROUNDED_SHELL(x, NO) ==> FAMILY(x,NOSHELL)'))
    kb.tell(expr('ORDER(x,SOFT) & JUMP(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,SOFT) & JUMP(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,SHELL) & TAIL(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,SHELL) & TAIL(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,CELLS) & STATIONARY(x, YES) ==> FAMILY(x,STATIONARY)'))
    kb.tell(expr('ORDER(x,CELLS) & STATIONARY(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('ORDER(x,STOMACH) & MULTICELLED(x, YES) ==> FAMILY(x,MULTICELLED)'))
    kb.tell(expr('ORDER(x,STOMACH) & MULTICELLED(x, NO) ==> TYPE_ANIMAL(x)'))

    kb.tell(expr('FAMILY(x,NOWINGS) & OPPOSING_THUMB(x, YES) ==> GENUS(x,THUMB)'))
    kb.tell(expr('FAMILY(x,NOWINGS) & OPPOSING_THUMB(x, NO) ==> GENUS(x,NOTHUMB)'))
    kb.tell(expr('FAMILY(x,HOOVES) & TWO_TOES(x, YES) ==> GENUS(x,TWOTOES)'))
    kb.tell(expr('FAMILY(x,HOOVES) & TWO_TOES(x, NO) ==> GENUS(x,ONETOE)'))
    kb.tell(expr('FAMILY(x,FEET) & LIVE_IN_WATER(x, YES) ==> GENUS(x,WATER)'))
    kb.tell(expr('FAMILY(x,FEET) & LIVE_IN_WATER(x, NO) ==> GENUS(x,DRY)'))
    kb.tell(expr('FAMILY(x,NOSHELL) & LIMBS(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('FAMILY(x,NOSHELL) & LIMBS(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('FAMILY(x,STATIONARY) & SPIKES(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('FAMILY(x,STATIONARY) & SPIKES(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('FAMILY(x,MULTICELLED) & SPIRAL_SHELL(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('FAMILY(x,MULTICELLED) & SPIRAL_SHELL(x, NO) ==> GENUS(x,NOSHELL)'))

    kb.tell(expr('GENUS(x,THUMB) & PREHENSILE_TAIL(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('GENUS(x,THUMB) & PREHENSILE_TAIL(x, NO) ==> SPECIES(x,NOTAIL)'))
    kb.tell(expr('GENUS(x,NOTHUMB) & OVER_400(x, YES) ==> SPECIES(x,400)'))
    kb.tell(expr('GENUS(x,NOTHUMB) & OVER_400(x, NO) ==> SPECIES(x,UNDER400)'))
    kb.tell(expr('GENUS(x,TWOTOES) & HORNS(x, YES) ==> SPECIES(x,HORNS)'))
    kb.tell(expr('GENUS(x,TWOTOES) & HORNS(x, NO) ==> SPECIES(x,NOHORNS)'))
    kb.tell(expr('GENUS(x,ONETOE) & PLATING(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('GENUS(x,ONETOE) & PLATING(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('GENUS(x,WATER) & HUNTED(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('GENUS(x,WATER) & HUNTED(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('GENUS(x,DRY) & FRONT_TEETH(x, YES) ==> SPECIES(x,TEETH)'))
    kb.tell(expr('GENUS(x,DRY) & FRONT_TEETH(x, NO) ==> SPECIES(x,NOTEETH)'))
    kb.tell(expr('GENUS(x,NOSHELL) & BIVALVE(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('GENUS(x,NOSHELL) & BIVALVE(x, NO) ==> TYPE_ANIMAL(x)'))

    kb.tell(expr('SPECIES(x,NOTAIL) & NEARLY_HAIRLESS(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,NOTAIL) & NEARLY_HAIRLESS(x, NO) ==> SUBSPECIES(x,HAIR)'))
    kb.tell(expr('SPECIES(x,400) & LAND_BASED(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,400) & LAND_BASED(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,UNDER400) & THINTAIL(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,UNDER400) & THINTAIL(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,NOHORNS) & LIVES_IN_DESERT(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,NOHORNS) & LIVES_IN_DESERT(x, NO) & SEMI_AQUATIC(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,NOHORNS) & LIVES_IN_DESERT(x, NO) & SEMI_AQUATIC(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,TEETH) & LARGE_EARS(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,TEETH) & LARGE_EARS(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,NOTEETH) & POUCH(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,NOTEETH) & POUCH(x, NO) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,HORNS) & FLEECE(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SPECIES(x,HORNS) & FLEECE(x, NO) ==> SUBSPECIES(x,NOFLEECE)'))

    kb.tell(expr('SUBSPECIES(x,HAIR) & LONG_POWERFUL_ARMS(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SUBSPECIES(x,HAIR) & LONG_POWERFUL_ARMS(x, NO) ==> TYPE_ANIMAL(x)'))

    kb.tell(expr('SUBSPECIES(x,NOFLEECE) & DOMESTICATED(x, YES) ==> TYPE_ANIMAL(x)'))
    kb.tell(expr('SUBSPECIES(x,NOFLEECE) & DOMESTICATED(x, NO) ==> TYPE_ANIMAL(x)'))


animal_kb()


def split_string_by_double_underscore(input_string):
    global answers
    answers = []
    if '__' in input_string:
        parts_array = input_string.split('__')
        return parts_array
    else:
        return [input_string]


def get_animals_list():
    global last_question_id
    global last_answer

    question_id = 1
    answers_copy = answers.copy()

    while question_id != 'end':

        last_question_id = question_id
        question = questions_list[question_id - 1]

        for answer in answers_copy:
            if answer == 'YES' or answer == 'NO':
                question_id = question[str.upper(answer)]
                answers_copy.remove(answer)
                last_answer = str.upper(answer)
                break

    animals = list(fol_fc_ask(kb, expr(rules[last_question_id - 1] + '(x,' + last_answer + ')')))
    return split_string_by_double_underscore(str.lower(str(animals[0][x])))


class ResultView(View):
    def get(self, request):
        if not answers:
            return HttpResponse("No answers provided", status=400)

        if next_question_id != "end":
            return HttpResponse("Not enough answers provided", status=400)

        try:
            animals_list = get_animals_list()
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}", status=500)

        return JsonResponse({'data': animals_list})


class FAQView(View):
    question_id = 1
    status = "next"

    def get(self, request):
        return JsonResponse({
            "id": 1,
            "question": str(questions_list[0]["question"]),
            "status": "next"
        })

    @csrf_exempt
    def post(self, request):
        answers_data = json.loads(request.body)
        print(answers_data)
        # Check the format of the request
        if 'id' not in answers_data or 'answer' not in answers_data:
            return HttpResponse("Invalid format: 'id' and 'answer' keys are required", status=400)

        # Retrieve values
        question_id = answers_data['id']
        answer_value = answers_data['answer']

        # Check if the id could be cast to an integer
        try:
            question_id = int(question_id)
        except ValueError:
            return HttpResponse("Invalid format: 'id' must be able to be casted to an integer", status=400)

        try:
            assert answer_value == 'yes' or answer_value == 'no'
        except AssertionError:
            return HttpResponse("Invalid format: 'answer' must have values in ['yes', 'no']", status=400)

        # Collect the answer
        global answers
        answers.append(str.upper(answer_value))

        # Prepare the response
        global next_question_id
        next_question_id = questions_list[question_id - 1][str.upper(answer_value)]

        if next_question_id == "end":
            self.question_id = -1
            self.status = "end"
            return JsonResponse({
                "id": str(self.question_id),
                "question": "None",
                "status": str(self.status)
            })

        self.question_id = next_question_id
        self.status = "next"

        return JsonResponse({
            "id": str(self.question_id),
            "question": str(questions_list[self.question_id - 1]["question"]),
            "status": str(self.status)
        })
