import sys ; input = sys.stdin.readline

pokemon_dict = dict()
N, M = map(int, input().split())

for i in range(N) :
    pokemon = input().rstrip()
    pokemon_dict[i + 1] = pokemon

convert_pokemon_dict = {
    value:key for key, value in pokemon_dict.items()
}

for _ in range(M) :
    question = input().rstrip()
    answer = ""
    
    if question.isnumeric() :
        answer = pokemon_dict.get(int(question))
    else :
        answer = convert_pokemon_dict.get(question)
    
    print(answer)