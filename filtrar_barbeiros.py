import json

def carregar_barbeiros(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def filtrar_barbeiros(barbeiros, min_avaliacao=0, max_preco=float('inf'), max_distancia=float('inf')):
    filtradas = []
    for b in barbeiros:
        if (
            b["avaliacao"] >= min_avaliacao and
            b["preco"] <= max_preco and
            b["distancia"] <= max_distancia
        ):
            filtradas.append(b)
    return filtradas

def main():
    barbeiros = carregar_barbeiros("BARBEIROS.json")

    min_avaliacao = float(input("Avaliação mínima: "))
    max_preco = float(input("Preço máximo: "))
    max_distancia = float(input("Distância máxima (km): "))

    resultados = filtrar_barbeiros(barbeiros, min_avaliacao, max_preco, max_distancia)

    print("\n--- Resultados da Busca ---")
    if resultados:
        for b in resultados:
            print(f"{b['nome']} | {b['avaliação']} | R${b['preço']} | {b['distância']} km")
    else:
        print("Nenhum barbeiro encontrado com esses filtros.")

if __name__ == "__main__":
    main()
