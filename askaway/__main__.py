import vercel_ai
import json
from tabulate import tabulate

def main():
    client = vercel_ai.Client()
    models = ''.join(json.dumps(client.model_ids))[1:-1].replace('\"', '').split(', ')
    models_table = []
    for i, model in enumerate(models):
        models_table.append(
            [i, model]
        )
    print(
        tabulate(
            models_table,
            headers=["#", "Model"],
            tablefmt="fancy_grid",
        )
    )
    model_choice = int(input("Choose a model #: "))
    prompt = input("Enter a prompt: ")
    for chunk in client.generate(models[model_choice], prompt):
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
